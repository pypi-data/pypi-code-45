#!/usr/bin/env python
# encoding: utf-8

import fnmatch
import os
import subprocess
from pathlib import Path

#import log
import might.might_log as mlog
from might.amr_methods import amr_precheck, ariba_run, amrfinderplus_run, summarize_amr_finder_output
from might.assembly_methods import assembly_precheck, adapter_trimming, run_unicycler_assembly, assembly_file_formatting, \
    filter_long_reads
from might.database_methods import database_check
from might.kraken_methods import kraken2_precheck, run_kraken2
from might.miscellaneous import parse_arguments, compression_handler, file_check, ascii_art


def premain():
    ascii_art(logo='might')
    args = parse_arguments(might=True)
    # use args to instantiate the IndividualSequencingSample object
    sample = IndividualSequencingSample(args)
    main(sample)


def main(sample):

    kraken2(sample)

    assembly(sample)

    amr(sample)

    cleanup(sample)


class IndividualSequencingSample:
    """
    object used to track the progress of an individual sample/isolate through the analysis pipeline. Primary usage is
    to determine if the input/output requirements of a given analysis are met before launching
    """

    def __init__(self, args):

        # self.name is the name of the sequencing sample. Provided at the command line, it should be the first field in
        # the fastq/fasta file followed by an '_'
        self.name = args.sample_name

        # self.output_directory is the parent directory which will store all of the output for this sample, as well as
        # any other samples being processed concurrently with AllMight.py. If it doesn't already exist, we will make it
        # here
        self.output_directory = Path(args.output).expanduser().resolve()
        if not self.output_directory.exists():
            subprocess.run(['mkdir', str(self.output_directory)])

        # self.logs_folder is output subdirectory where all of the might log files are stored
        self.logs_folder = self.output_directory / 'logs'
        if not self.logs_folder.exists():
            subprocess.run(['mkdir', str(self.logs_folder)])

        # self.log is the path to the log file for this sample
        self.log_file = self.logs_folder / (self.name + '.might.log')

        # if the verbosity levels are specified
        self.stdout_verbosity = int(args.verbosity)

        self.log_file_verbosity = 4

        # ALT: Use the this object to track the log object attributes, and use the static methods
        mlog.initialize_logger_attributes(self,
                                          log_filename=self.log_file,
                                          stdout_verbosity_level=self.stdout_verbosity,
                                          log_file_verbosity_level=self.log_file_verbosity)

        # self.reads_directory is the parent directory for all read files that are GENERATED during an analysis. These
        # include raw_reads if bcl2fastq2 was run via AllMight.py as well as processed reads if read trimming was
        # performed as part of the assembly analysis
        self.reads_directory = self.output_directory / 'reads'
        if not self.reads_directory.exists():
            subprocess.run(['mkdir', str(self.reads_directory)])

        # self.raw_reads_directory is set at the command line, and could refer to a directory within the output/reads
        # directory (in the case where AllMight.py generated fastqs via bcl2fastq2) or a user specified directory where
        # the read files for the current sample are located
        if args.fastq:
            self.raw_reads_directory = Path(args.fastq).expanduser().resolve()
        else:
            self.raw_reads_directory = self.reads_directory / 'raw_reads'

        # self.processed_reads_directory is a subdirectory of the reads directory and will contain any trimmed read
        # files that are generated if --assembly is specified
        self.processed_reads_directory = self.reads_directory / 'processed_reads'

        # self.r1_fastq and self.r2_fastq refer to the Illumina paired end R1 and R2 read files, respectively. They are
        # initialized as None type and then automatically assigned the file paths using scan_for_fastq(), assuming the
        # files exist
        self.r1_fastq = None
        self.r2_fastq = None
        if args.fastq:
            self.scan_for_fastq()

        # self.raw_long_reads_file refers to the user specified long reads file in fastq format
        if args.long_reads:
            self.raw_long_reads_file = args.long_reads

        # self.assembly is used to store the path to the assembled contigs file. It is initialized as None type and then
        # automatically assigned the file paths using scan_for_fasta(), assuming the file exists
        self.assembly_file = None
        if args.fasta:
            self.scan_for_assembly(args.fasta)

        # self.force is set at the command line. If set to true, it will overwrite all existing output it comes across
        # for this sample. Use with caution!
        self.force = args.force

        # self.ramdisk will store the path to the prepared ramdisk if provided at the command line, or None if it was
        # not specified.
        if args.ramdisk:
            self.ramdisk = Path(args.ramdisk).expanduser().resolve()
        else:
            self.ramdisk = None

        # self.cores is the number of cores, stored as a string, that are available for this sample's analysis
        self.cores = str(args.cores)

        # kraken2 analysis specific path attributes. They are only set to non-None values if Kraken2 analysis is
        # requested. kraken2 database presence is validated during argument parsing
        self.kraken2 = args.kraken2
        if self.kraken2:

            self.kraken2_database = Path(args.kraken2_database).expanduser().resolve()

            # self.kraken2_directory is the parent directory for all kraken2 output
            self.kraken2_directory = self.output_directory / 'kraken2'

            # self.kraken2_report is the path to the output of a kraken2 analysis run
            self.kraken2_report = self.kraken2_directory / (self.name + '_kraken2_report.txt')

        # assembly specific file paths. Like the Kraken2 attributes these file path attributes are only instantiated if
        # assembly is requested
        self.assembly = args.assembly
        if args.assembly:

            # self.assembly_directory is the parent directory for all assembly output
            self.assembly_directory = self.output_directory / 'assembly'

            # self.individual_assembly_directory is the parent directory for all files and directories generated during
            # assembly pertaining to this sample
            self.individual_assembly_directory = self.assembly_directory / self.name

            # self.adapter_file
            self.adapter_file = Path(args.adapter_file).expanduser().resolve()
            self.r1_fastq_trimmed = self.processed_reads_directory / (self.name + '_r1_trimmed.fastq')
            self.r2_fastq_trimmed = self.processed_reads_directory / (self.name + '_r2_trimmed.fastq')

        # amr specific file paths, instantiated only if amr is analysis is requested
        self.amr = args.amr
        if args.amr:

            # self.amr_directory is the parent directory for all amr analysis. If it doesn't exist, generate it
            self.amr_directory = self.output_directory / 'amr'
            if not self.amr_directory.exists():
                subprocess.run(['mkdir', str(self.amr_directory)])

            # self.individual_amr_directory is the parent directory for all files and directories generated during
            # amr analysis of this sample
            self.individual_amr_directory = self.amr_directory / self.name

            # self.ariba_output_directory stores all of the output files and directories generated by ARIBA if amr
            # analysis is performed using read data
            self.ariba_output_directory = self.individual_amr_directory / 'ARIBA_output'
            self.ariba_assembled_genes = self.ariba_output_directory / 'assembled_genes.fa.gz'
            self.ariba_assemblies = self.ariba_output_directory / 'assemblies.fa.gz'

            # file paths to all of the amr analysis output files
            self.amrfinder_output_from_ariba = self.individual_amr_directory / 'amrfinder_output_from_ariba.txt'
            self.amrfinder_output_from_contigs = self.individual_amr_directory / 'amrfinder_output_from_contigs.txt'
            self.amr_output_file = self.individual_amr_directory / 'andale_output_raw.csv'

        # mlst specific file paths
        if args.mlst:

            self.mlst = args.mlst

            self.mlst_directory = self.output_directory / 'mlst'
            self.mlst_assignment_file = ""

        # plasmidfinder specific file paths
        if args.plasmidfinder:

            self.plasmidfinder = args.plasmidfinder

            self.plasmidfinder_directory = self.output_directory / 'plasmidfinder'
            self.plasmidfinder_results_file = ""

        self.pbs_script_directory = self.output_directory / 'pbs_scripts'

        self.update = args.update

    def scan_for_fastq(self, directory=None):
        """
        scans the specified directory (default is output/reads/raw_reads/) for fastq files that match the name of the
        sample, then assigns their POSIX paths to the self.r1_fastq and self.r2_fastq object attributes. Finally, method
        returns True if both the r1 and r2 files were located, False if they were not
        """
        if directory:
            directory = Path(directory).expanduser().resolve()
        else:
            directory = self.raw_reads_directory

        for file in os.scandir(directory):
            if file.name.startswith(self.name+"_") and fnmatch.fnmatch(file, '*R1*fastq*'):
                self.r1_fastq = Path(file).expanduser().resolve()
            elif file.name.startswith(self.name+"_") and fnmatch.fnmatch(file, '*R2*fastq*'):
                self.r2_fastq = Path(file).expanduser().resolve()

    def scan_for_assembly(self, directory=None):
        """
        scans the specified directory (default is output/assembly/<sample name>/) for fna file that match the name of the
        sample, then assigns the POSIX path to the self.assembly object attributes
        """

        if directory:
            directory = Path(directory).expanduser().resolve()
        else:
            if file_check(self.output_directory / 'assembly' / self.name):
                directory = self.output_directory / 'assembly' / self.name

        for file in os.scandir(directory):
            if file.name.startswith(self.name + '_') and (fnmatch.fnmatch(file, '*.fasta*') or fnmatch.fnmatch(file, '*.fna*')):
                self.assembly_file = Path(file).expanduser().resolve()
                return

        if self.assembly:
            for file in os.scandir(directory):
                if fnmatch.fnmatch(file, 'assembly.fasta'):
                    self.assembly_file = Path(file).expanduser().resolve()
                    return


def kraken2(sample):
    """
    KRAKEN2 ANALYSIS
    """
    if sample.kraken2:

        mlog.log_section_header('Kraken2 - Species/contamination prediction from read files',
                                colors=sample.colors,
                                stdout_verbosity_level=sample.stdout_verbosity,
                                log_file_verbosity_level=sample.log_file_verbosity,
                                log_file=sample.log_file)
        mlog.log_explanation('Kraken 2 is the newest version of Kraken, a taxonomic classification system using'
                             ' exact k-mer matches to achieve high accuracy and fast classification speeds. '
                             'This classifier matches each k-mer within a query sequence to the lowest common '
                             'ancestor (LCA) of all genomes containing the given k-mer. The k-mer assignments '
                             'inform the classification algorithm.  The output from this analysis currently '
                             'requires manual curation to validate a) species classification and b) '
                             'contamination detection.',
                             colors=sample.colors,
                             stdout_verbosity_level=sample.stdout_verbosity,
                             log_file_verbosity_level=sample.log_file_verbosity,
                             log_file=sample.log_file)

        # scan for Illumina read files
        mlog.log('scanning for input files...',
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)
        sample.scan_for_fastq()
        mlog.log('Current value for R1: ' + mlog.green(str(sample.r1_fastq)),
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)
        mlog.log('Current value for R2: ' + mlog.green(str(sample.r2_fastq)) + '\n',
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)

        if kraken2_precheck(kraken2_database=sample.kraken2_database,
                            force=sample.force,
                            kraken2_directory=sample.kraken2_directory,
                            kraken2_report=sample.kraken2_report,
                            r1_fastq=sample.r1_fastq,
                            r2_fastq=sample.r2_fastq,
                            colors=sample.colors,
                            stdout_verbosity_level=sample.stdout_verbosity,
                            log_file_verbosity_level=sample.log_file_verbosity,
                            log_file=sample.log_file):

            # check that the read files are not compressed
            compression_handler(sample, 'decompress', ['r1_fastq', 'r2_fastq'])
            # run kraken2
            run_kraken2(kraken2_database=sample.kraken2_database,
                        kraken2_report=sample.kraken2_report,
                        r1_fastq=sample.r1_fastq,
                        r2_fastq=sample.r2_fastq,
                        ramdisk=sample.ramdisk,
                        threads=sample.cores,
                        colors=sample.colors,
                        stdout_verbosity_level=sample.stdout_verbosity,
                        log_file_verbosity_level=sample.log_file_verbosity,
                        log_file=sample.log_file)


def assembly(sample):
    """
    ASSEMBLY
    """
    if sample.assembly:

        mlog.log_section_header('Assembly Prechecks',
                                colors=sample.colors,
                                stdout_verbosity_level=sample.stdout_verbosity,
                                log_file_verbosity_level=sample.log_file_verbosity,
                                log_file=sample.log_file)
        mlog.log_explanation('Determine if the requisite conditions have been met to perform adapter trimming with '
                             'bbduk and then assembly using Unicycler. If long read data was provided, preprocess it '
                             'with filtlong.',
                             colors=sample.colors,
                             stdout_verbosity_level=sample.stdout_verbosity,
                             log_file_verbosity_level=sample.log_file_verbosity,
                             log_file=sample.log_file)

        # scan for Illumina read files
        mlog.log('scanning for input files...',
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)
        sample.scan_for_fastq()
        mlog.log('Current value for R1: ' + mlog.green(str(sample.r1_fastq)),
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)
        mlog.log('Current value for R2: ' + mlog.green(str(sample.r2_fastq)) + '\n',
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)
        # update the assembly file attribute
        sample.scan_for_assembly()
        mlog.log('Current value for assembly is: ' + mlog.green(str(sample.assembly_file)) + '\n',
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)

        # perform the assembly precheck to a) validate that an assembly can be performed and b) if that assembly will
        # include long read data
        precheck = assembly_precheck(r1_fastq=sample.r1_fastq,
                                     r2_fastq=sample.r2_fastq,
                                     raw_long_reads_file=sample.raw_long_reads_file,
                                     individual_assembly_directory=sample.individual_assembly_directory,
                                     assembly=sample.assembly_file,
                                     force=sample.force,
                                     colors=sample.colors,
                                     stdout_verbosity_level=sample.stdout_verbosity,
                                     log_file_verbosity_level=sample.log_file_verbosity,
                                     log_file=sample.log_file)

        if not precheck:
            return

        # check that the short read files are not compressed
        compression_handler(sample, 'decompress', ['r1_fastq', 'r2_fastq'])

        # perform adapter trimming
        trim_check = adapter_trimming(r1_fastq=sample.r1_fastq,
                                      r2_fastq=sample.r2_fastq,
                                      r1_fastq_trimmed=sample.r1_fastq_trimmed,
                                      r2_fastq_trimmed=sample.r2_fastq_trimmed,
                                      adapter_file=sample.adapter_file,
                                      force=sample.force,
                                      colors=sample.colors,
                                      stdout_verbosity_level=sample.stdout_verbosity,
                                      log_file_verbosity_level=sample.log_file_verbosity,
                                      log_file=sample.log_file)

        if not trim_check:
            return

        # if precheck = 'long', we will attempt to preprocess the long read data now
        if precheck == 'long':

            sample.processed_long_reads = sample.processed_reads_directory / (sample.name + '_processed_long_reads.fastq')

            long_read_filter = filter_long_reads(r1_fastq=sample.r1_fastq_trimmed,
                                                 r2_fastq=sample.r2_fastq_trimmed,
                                                 raw_long_reads=sample.raw_long_reads,
                                                 processed_long_reads=sample.processed_long_reads,
                                                 force=sample.force,
                                                 colors=sample.colors,
                                                 stdout_verbosity_level=sample.stdout_verbosity,
                                                 log_file_verbosity_level=sample.log_file_verbosity,
                                                 log_file=sample.log_file)

            # determine the long read settings based on the results of the long read filtering
            if long_read_filter:
                long_read_file_for_assembly = sample.processed_long_reads
            else:
                long_read_file_for_assembly = sample.raw_long_reads
        else:
            long_read_file_for_assembly = None

        # perform unicycler assembly
        run_unicycler_assembly(r1_fastq_trimmed=sample.r1_fastq_trimmed,
                               r2_fastq_trimmed=sample.r2_fastq_trimmed,
                               long_read_file=long_read_file_for_assembly,
                               mode=precheck,
                               individual_assembly_directory=sample.individual_assembly_directory,
                               threads=sample.cores)

        # compress the trimmed read files
        compression_handler(sample, 'compress', ['r1_fastq_trimmed', 'r2_fastq_trimmed'])

        # update the assembly file attribute
        sample.scan_for_assembly()

        # copy the unicycler log file to the might log file
        unicycler_log_file = sample.individual_assembly_directory / 'unicycler.log'
        mlog.log('',
                 colors=sample.colors,
                 stdout_verbosity_level=0,
                 log_file_verbosity_level=sample.log_file_verbosity_level,
                 log_file=sample.log_file)
        with open(str(unicycler_log_file), 'r') as uni_log:
            for line in uni_log.readlines():
                mlog.log(str(line),
                         colors=sample.colors,
                         stdout_verbosity_level=0,
                         log_file_verbosity_level=sample.log_file_verbosity_level,
                         log_file=sample.log_file)

        # reformat the assembly file
        compression_handler(sample, 'decompress', ['assembly_file'])

        assembly_file_formatting(assembly_file=(sample.individual_assembly_directory / 'assembly.fasta'),
                                 sample_name=sample.name,
                                 colors=sample.colors,
                                 stdout_verbosity_level=sample.stdout_verbosity,
                                 log_file_verbosity_level=sample.log_file_verbosity,
                                 log_file=sample.log_file)


def amr(sample):
    """
    AMR Prediction
    """
    if sample.amr:

        mlog.log_section_header('Andale AMR Identification',
                                colors=sample.colors,
                                stdout_verbosity_level=sample.stdout_verbosity,
                                log_file_verbosity_level=sample.log_file_verbosity,
                                log_file=sample.log_file)
        mlog.log_explanation('Use Andale to perform AMR Identification based on the available files. ',
                             colors=sample.colors,
                             stdout_verbosity_level=sample.stdout_verbosity,
                             log_file_verbosity_level=sample.log_file_verbosity,
                             log_file=sample.log_file)

        #ascii_art(logo='andale')

        # scan for fastq and assembly files
        mlog.log('Updating read file attributes',
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)
        sample.scan_for_fastq()
        mlog.log('Current value for R1: ' + mlog.green(str(sample.r1_fastq)),
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)
        mlog.log('Current value for R2: ' + mlog.green(str(sample.r2_fastq)) + '\n',
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)
        mlog.log('Updating assembly file attributes',
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)
        sample.scan_for_assembly()
        mlog.log('Current value for assembly: ' + mlog.green(str(sample.assembly_file)) + '\n',
                 colors=sample.colors,
                 stdout_verbosity_level=sample.stdout_verbosity,
                 log_file_verbosity_level=sample.log_file_verbosity,
                 log_file=sample.log_file)

        # determine if the requested analysis type is valid, downgrade or switch if necessary
        sample.amr_analysis_type = amr_precheck(r1_fastq=sample.r1_fastq,
                                                r2_fastq=sample.r2_fastq,
                                                assembly=sample.assembly_file,
                                                individual_amr_directory=sample.individual_amr_directory,
                                                analysis_type=sample.amr,
                                                force=sample.force,
                                                colors=sample.colors,
                                                stdout_verbosity_level=sample.stdout_verbosity,
                                                log_file_verbosity_level=sample.log_file_verbosity,
                                                log_file=sample.log_file)

        # If the amr_precheck() method returned a non-None analysis type, verify the required databases are present and
        # run the analysis
        if sample.amr_analysis_type:

            # verify the databases are installed
            sample.amrfinder_database, sample.ariba_database = database_check(update=sample.update,
                                                                              colors=sample.colors,
                                                                              stdout_verbosity_level=sample.stdout_verbosity,
                                                                              log_file_verbosity_level=sample.log_file_verbosity,
                                                                              log_file=sample.log_file)

            # create the individual_amr_directory
            if not sample.individual_amr_directory.exists():
                subprocess.run(['mkdir', str(sample.individual_amr_directory)])

            # run the validated analyses
            if sample.amr_analysis_type == 'combination' or sample.amr_analysis_type == 'reads':
                if ariba_run(sample,
                             colors=sample.colors,
                             stdout_verbosity_level=sample.stdout_verbosity,
                             log_file_verbosity_level=sample.log_file_verbosity,
                             log_file=sample.log_file):
                    amrfinderplus_run(sample,
                                      ['ariba_assemblies', 'amrfinder_output_from_ariba'],
                                      'reads',
                                      colors=sample.colors,
                                      stdout_verbosity_level=sample.stdout_verbosity,
                                      log_file_verbosity_level=sample.log_file_verbosity,
                                      log_file=sample.log_file)
            if sample.amr_analysis_type == 'combination' or sample.amr_analysis_type == 'contigs':
                amrfinderplus_run(sample,
                                  ['assembly_file', 'amrfinder_output_from_contigs'],
                                  'contigs',
                                  colors=sample.colors,
                                  stdout_verbosity_level=sample.stdout_verbosity,
                                  log_file_verbosity_level=sample.log_file_verbosity,
                                  log_file=sample.log_file)

            # summarize the results
            summarize_amr_finder_output(sample,
                                        colors=sample.colors,
                                        stdout_verbosity_level=sample.stdout_verbosity,
                                        log_file_verbosity_level=sample.log_file_verbosity,
                                        log_file=sample.log_file)


def cleanup(sample):
    """
    CLEANUP
    """
    mlog.log_section_header('Clean up',
                            colors=sample.colors,
                            stdout_verbosity_level=sample.stdout_verbosity,
                            log_file_verbosity_level=sample.log_file_verbosity,
                            log_file=sample.log_file)
    mlog.log_explanation('Analysis is complete. We will now compress large files',
                         colors=sample.colors,
                         stdout_verbosity_level=sample.stdout_verbosity,
                         log_file_verbosity_level=sample.log_file_verbosity,
                         log_file=sample.log_file)

    compression_handler(sample, 'compress', ['r1_fastq', 'r2_fastq'])

    mlog.log_section_header('All done',
                            colors=sample.colors,
                            stdout_verbosity_level=sample.stdout_verbosity,
                            log_file_verbosity_level=sample.log_file_verbosity,
                            log_file=sample.log_file)
    mlog.log_explanation('Thanks for using Might!',
                         colors=sample.colors,
                         stdout_verbosity_level=sample.stdout_verbosity,
                         log_file_verbosity_level=sample.log_file_verbosity,
                         log_file=sample.log_file)

    ascii_art('might')

if __name__ == '__main__':
    premain()
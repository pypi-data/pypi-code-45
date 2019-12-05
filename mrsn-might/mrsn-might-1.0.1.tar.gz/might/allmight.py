#!/usr/bin/env python
# encoding: utf-8
import copy
import multiprocessing as mp
import os
import subprocess
import sys
from fnmatch import fnmatch
from math import ceil
from multiprocessing import Pool
from pathlib import Path
import might_log as mlog
from database_methods import database_check
from miscellaneous import parse_arguments, check_for_dependency, quit_with_error, validate_sample_sheet, \
    ramdisk_handler, round_down, ascii_art


def main():

    ascii_art('might')

    args = parse_arguments(allmight=True)

    # make sure that the output directory exists
    args.output_directory = Path(args.output).expanduser().resolve()
    if not args.output_directory.exists():
        subprocess.run(['mkdir', str(args.output_directory)])

    # make sure that the reads/raw_reads subdirectory of the output directory exists
    raw_reads_directory = args.output_directory / 'reads' / 'raw_reads'
    if not raw_reads_directory.exists():
        subprocess.run(['mkdir', '-p', str(raw_reads_directory)])

    # a sample list should have been generated during parse_arguments. Set it to sample_list for use here
    sample_list = args.sample_list

    # If bcl2fastq2 analysis is requested, parse_arguments() should have validated the sample sheet, copied it to the
    # required directory and produced a list of the samples we are expecting to have data for.
    if args.bcl2fastq:
        sample_list = bcl2fastq2(sample_sheet=args.sample_sheet,
                                 run_directory=args.run_directory,
                                 sample_list=args.sample_list,
                                 cores=args.cores)

        # Sanity check: make sure that we got samples back bcl2fastq2
        if len(sample_list) == 0:
            quit_with_error('ERROR: bcl2fastq2 returned no samples for analysis!')

        # We are going to move the fastq files for the good samples to the reads/raw_reads subdirectory of the output
        # directory. If the reads for a given sample are already present, we will abort analysis of this sample and
        # report that to the user.

        for sample in sample_list:
            for file in os.scandir(str(raw_reads_directory)):
                if file.name.startswith(sample + '_'):
                    mlog.log('WARNING: ' + sample + ' already has read files present in the output/reads/raw_reads '
                            'directory! This sample will be omitted from analysis.')
                    sample_list.remove(sample)

        # Sanity check: make sure that we still have samples to analyze
        if len(sample_list) == 0:
            quit_with_error('There are no new samples for analysis! Please remove old read files from the output '
                            'directory, or specify a new output directory')

        for sample in sample_list:
            for file in os.scandir(str(Path(args.run_directory).expanduser().resolve() / 'Data' / 'Intensities' / 'BaseCalls')):
                if file.name.startswith(sample + '_'):
                    subprocess.run(['mv', file, str(raw_reads_directory)])

        # If no other analyses were requested, we will exit here. All that follows pertains to individual parallel
        # analyses
        if not args.kraken2 and not args.assembly and not args.amr:
            mlog.log('Since only bcl2fastq was requested, AllMight.py is finished. Your fastq files can be found here'
                    ':\n' + str(raw_reads_directory))
            sys.exit()

    # If kraken2 analysis was requested by the user, lets go ahead and mount the ramdisk now
    if args.kraken2:
        if not ramdisk_handler(mount=True,
                               ramdisk_directory=args.ramdisk,
                               directory_to_load=args.kraken2_database):
            args.ramdisk=None

    # If amr analysis was requested or a database update was requested, lets verify or install the amr databases now
    if args.amr:
        database_check(update=args.update)

    # Initialize parallel processing of the samples
    mlog.log_section_header('Starting Individual Analysis')
    mlog.log_explanation('Sample objects will be processed in parallel based on the parameters given')

    mp.set_start_method('spawn')
    pool_size = int(round_down(int(args.cores), 4) / 4)

    if int(args.cores) > 4:
        args.cores = '4'

    sample_arg_list = queue_loader(sample_list=sample_list, args=args, raw_reads_directory=raw_reads_directory)

    individual_samples = []

    for entry in sample_arg_list:
        individual_samples.append(Might.IndividualSequencingSample(entry))

    # run kraken2 analysis for all samples in parallel if requested
    if args.kraken2:
        p = Pool(pool_size)
        p.map(Might.kraken2, individual_samples)
        p.close()
        p.join()

    # run assembly analysis for all samples in parallel
    if args.assembly:
        p = Pool(pool_size)
        p.map(Might.assembly, individual_samples)
        p.close()
        p.join()

    # run amr analysis for all samples in parallel
    if args.amr:
        p = Pool(pool_size)
        p.map(Might.amr, individual_samples)
        p.close()
        p.join()

    # Clean up
    p = Pool(pool_size)
    p.map(Might.cleanup, individual_samples)
    p.close()
    p.join()

    ramdisk_handler(unmount=True, ramdisk_directory=str(args.ramdisk))


def bcl2fastq2(sample_sheet=None, run_directory=None, sample_list=None, cores='1'):
    """
    run bcl2fastq2 using SampleSheet.csv and the path to the run directory it resides in
    """

    mlog.log_section_header('bcl2fastq2')
    mlog.log_explanation('bcl2fastq2 demultiplexes sequencing data and converts base call (BCL) files into fastq files')

    if not sample_sheet or not run_directory:
        quit_with_error('bcl2fastq2 requires both a valid sample sheet and the path to the Illumina run '
                        'directory!')

    # determine if bcl2fastq2 is in PATH
    if not check_for_dependency('bcl2fastq'):
        quit_with_error('Unable to locate bcl2fastq2 in your path!')

    # bcl2fastq2 automatically generates fastq files in the [run directory]/Data/Intensities/BaseCalls directory
    basecalls_directory = Path(run_directory).expanduser().resolve() / 'Data' / 'Intensities' / 'BaseCalls'

    # make sure we are not overwriting any existing files. To do this, we will scan the basecalls_directory for any
    # fastq.gz files. If any are present, we will abort and prompt the user to clean this directory of any existing
    # bcl2fastq2 output

    for file in os.scandir(str(basecalls_directory)):
        if fnmatch(file, '*fastq*'):
            quit_with_error('There are already fastq files in the BaseCalls directory! If you wish to perform '
                            'bcl2fastq on this run directory, you will need to remove all fastq files!')

    # make sure that a sample_list was passed to the method, as this signals that the sample_sheet file was already
    # validated during parse_arguments(). If sample_list is None, we will run the validate_sample_sheet() now.

    if not sample_list:

        if not Path(run_directory).expanduser().resolve().is_dir():
            quit_with_error('User requested bcl2fastq2 be performed, but the path to the Illumina run output '
                            'directory provided by the user cannot be located.\n Please ensure that the path to the'
                            ' Illumina run output directory provided using --run-directory is correct!')
        if not Path(sample_sheet).expanduser().resolve().exists():
            quit_with_error('User requested bcl2fastq2 be performed, but the path provided to the SampleSheet.csv '
                            'file can not be verified.\n Please ensure that the path to the SampleSheet.csv file '
                            'provided using --sample-sheet is correct!')
        # validate the formatting of the SampleSheet.csv file before proceeding
        sample_list, sample_sheet = validate_sample_sheet(samplesheet=sample_sheet, run_directory=run_directory)

    # At this point, we should have a valid sample_sheet file in the run_directory as well as a BaseCalls subdirectory
    # that is free of prior bcl2fastq2 results. Time to boogie.

    # Determine the appropriate thread allocations for the run
    # --loading-threads: default is 4. Only change if the number of allotted processors is <4
    if int(cores) < 4:
        loading_threads = str(cores)
    else:
        loading_threads = '4'
    # --processing_threads: default is... as many as you are willing to give it.
    processing_threads = str(cores)
    # --writing threads: default is 4. Only change if the number of allotted processors is <4
    if int(cores) < 4:
        writing_threads = str(cores)
    else:
        writing_threads = '4'

    # prepare the bcl2fastq2 command as a string for logging purposes
    bcl2fastq2_cmd = 'bcl2fastq --runfolder-dir ' + str(Path(run_directory).expanduser().resolve()) + \
                     ' --loading-threads ' + loading_threads + ' --processing-threads ' + processing_threads + \
                     ' --writing-threads ' + writing_threads + ' --barcode-mismatches=1 --no-lane-splitting'

    mlog.log('Command: ' + mlog.bold(bcl2fastq2_cmd) + '\n')

    mlog.log('Running bcl2fastq...')

    subprocess.run(['bcl2fastq',
                    '--runfolder-dir', str(Path(run_directory).expanduser().resolve()),
                    '--loading-threads', loading_threads,
                    '--processing-threads', processing_threads,
                    '--writing-threads', writing_threads,
                    '--barcode-mismatches=1',
                    '--no-lane-splitting'],
                   stderr=subprocess.DEVNULL)

    mlog.log('bcl2fastq2 finished\n')

    # verify that bcl2fastq2 produced at least some fastq files
    bcl2fastq2_status = False
    for file in os.scandir(str(basecalls_directory)):
        if fnmatch(file, '*fastq*'):
            bcl2fastq2_status = True
            break

    if not bcl2fastq2_status:
        quit_with_error('bcl2fastq2 failed to produce any fastq.gz files in the expected location!')

    # verify that bcl2fastq2 produced at least some non 'Undetermined' files, otherwise exit with an error message
    # indicating there is likely a problem with the supplied sample sheet

    bcl2fastq2_status = False
    for file in os.scandir(str(basecalls_directory)):
        if not file.name.startswith('Undetermined') and fnmatch(file, '*fastq*'):
            bcl2fastq2_status = True
            break

    if not bcl2fastq2_status:
        quit_with_error('bcl2fastq2 only produced Undetermined files! Make sure that the sample sheet that you provided'
                        ' is the correct one for the run being analyzed')

    # Determine which samples we successfully generated fastq files for. Determine the size of the fastq output files
    # for each sample. If the files are below a certain size threshold, we will report them as sequencing failures to
    # the user and omit them from any downstream analysis.

    passed_sample_list = []

    for sample in sample_list:
        passed_reads = []
        for file in os.scandir(str(basecalls_directory)):
            if file.name.startswith(sample + '_') and fnmatch(file, '*R1*fastq*') and os.path.getsize(file)>20000000:
                passed_reads.append(file)
            if file.name.startswith(sample + '_') and fnmatch(file, '*R2*fastq*') and os.path.getsize(file)>20000000:
                passed_reads.append(file)
        if len(passed_reads) == 2:
            passed_sample_list.append(sample)

    for sample in sample_list:
        if sample not in passed_sample_list:
            mlog.log('WARNING: ' + mlog.bold(sample) + ' failed to produce quality read files and will be omitted from'
                    ' further analysis')

    # Acceptable losses filter. If more than 10% of isolates fail to pass the initial read size filter, quit with an
    # error asking the user to review the sample sheet for errors. This filter can be overridden with the --no-filters
    # option at the command line

    failure_threshold = ceil(len(sample_list)*0.1)
    failure_count = len(sample_list) - len(passed_sample_list)

    if failure_count > failure_threshold:
        quit_with_error('More than 10% of samples from this run failed to meet to the criteria for analysis. Please '
                        'review the sample sheet as well as library quantification data to ensure that this level of '
                        'sample failure is expected. If so, you can rerun the analysis with the --no-filter option')

    mlog.log('bcl2fastq complete!')
    # Return the list of samples that passed the size threshold for individual analysis
    return passed_sample_list


def queue_loader(sample_list=None, args=None, raw_reads_directory=None):

    sample_arg_list = []
    for sample in sample_list:
        sample_args = copy.copy(args)
        sample_args.sample_name = sample
        sample_args.fastq = str(raw_reads_directory)
        sample_args.fasta = None
        sample_args.verbosity = args.verbosity
        sample_args.log_file_verbosity = 4
        sample_arg_list.append(sample_args)
    return sample_arg_list


if __name__ == '__main__':
    main()


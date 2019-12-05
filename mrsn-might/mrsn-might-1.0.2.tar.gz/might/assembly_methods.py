#!/usr/bin/env python
# encoding: utf-8

import subprocess
from pathlib import Path

from Bio import SeqIO

import might.might_log as mlog
from might.miscellaneous import check_for_dependency, file_check


def assembly_precheck(r1_fastq=None, r2_fastq=None, raw_long_reads_file=None, individual_assembly_directory=None,
                      assembly=None, force=False, colors=1, stdout_verbosity_level=1, log_file_verbosity_level=1,
                      log_file=None):
    """
    for assembly to run, must have:
        1) unicycler on PATH
        2) r1_fastq and r2_fastq detected
        3) output directory does NOT already exist
    """

    # validate that the bbduk.sh adapter trimming program is on the PATH
    if not check_for_dependency('bbduk.sh'):
        mlog.log('Could not find bbduk on your PATH, so this analysis is being aborted',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False
    else:
        mlog.log('utility located: bbduk',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # validate that the unicycler assembly program is on the PATH
    if not check_for_dependency('unicycler'):
        mlog.log('Could not find Unicycler on your PATH, so this analysis is being aborted',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False
    else:
        mlog.log('utility located: unicycler',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # validate that the illumina paired end read files are present
    if not file_check(r1_fastq) or not file_check(r2_fastq):
        mlog.log('Could not find both read files, so this analysis is being aborted',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False
    else:
        mlog.log('R1 and R2 read files located',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # validate that the raw_long_reads file exists
    if not file_check(raw_long_reads_file):
        mlog.log('The long reads file could not be located, so the long reads will not be used!',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        raw_long_reads_file = None
    else:
        mlog.log('raw long reads files located',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # check to see if the individual_assembly_directory exists already. If so, check to see if the output assembly.fasta
    # is already present.
    if file_check(individual_assembly_directory):
        if file_check(assembly):
            if force:
                mlog.log('Unicycler output for this sample was already present, but --force was invoked so we will '
                         'overwrite the existing results',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
                subprocess.run(['rm', str(individual_assembly_directory)])
            else:
                mlog.log('Unicycler output for this sample was already present, so this analysis is being aborted\n',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
                return False

    mlog.log('Assembly precheck passed: sample ready for adapter trimming and assembly!',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    # return the assembly type. If short reads ONLY are present, return "short". If BOTH short and long reads are
    # present, return "long"

    if raw_long_reads_file:
        return 'long'
    else:
        return 'short'


def adapter_trimming(r1_fastq=None, r2_fastq=None, r1_fastq_trimmed=None, r2_fastq_trimmed=None, adapter_file=None,
                     force=False, colors=1, stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None):
    """
    perform adapter trimming on the raw fastq files
    """

    mlog.log_section_header('Adapter Trimming',
                            colors=colors,
                            stdout_verbosity_level=stdout_verbosity_level,
                            log_file_verbosity_level=log_file_verbosity_level,
                            log_file=log_file)
    mlog.log_explanation('Perform adapter (and light quality) trimming of Illumina read files using bbduk.',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)

    # validate the adapter_fa_file
    if not file_check(adapter_file):
        mlog.log('cannot locate the adapter.fa file for bbduk trimming, aborting assembly',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False

    # check for preexisting adapter trimmed files
    if file_check(r1_fastq_trimmed) and file_check(r2_fastq_trimmed):
        if force:
            subprocess.run(['rm', str(r1_fastq_trimmed)])
            subprocess.run(['rm', str(r2_fastq_trimmed)])
        else:
            mlog.log('trimmed read files located, so skipping adapter trimming with bbduk',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            return True

    # if only one of the two trimmed read files is present, remove it and redo the trimming
    if file_check(r1_fastq_trimmed) and not file_check(r2_fastq_trimmed):
        subprocess.run(['rm', str(r1_fastq_trimmed)])
    elif not file_check(r1_fastq_trimmed) and file_check(r2_fastq_trimmed):
        subprocess.run(['rm', str(r2_fastq_trimmed)])

    # prepare the adapter trimming cmd as a string
    adapter_trimming_cmd = 'bbduk.sh in1=' + str(r1_fastq) + ' in2=' + str(r2_fastq) + ' out1=' + str(r1_fastq_trimmed) \
                           + " out2=" + str(r2_fastq_trimmed) + " ref= " + str(adapter_file) + 'ktrim=r k=23' \
                            ' mink=11 hdist=1 tpe tbo qtrim=r trimq=8'

    mlog.log('Command: ' + mlog.bold(adapter_trimming_cmd) + '\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    # run the adapter trimming command
    bbduk_proc = subprocess.run(['bbduk.sh',
                                 'in1=' + str(r1_fastq),
                                 'in2=' + str(r2_fastq),
                                 'out1=' + str(r1_fastq_trimmed),
                                 'out2=' + str(r2_fastq_trimmed),
                                 'ref=' + str(adapter_file),
                                 'ktrim=r',
                                 'k=23',
                                 'mink=11',
                                 'hdist=1',
                                 'tpe',
                                 'tbo',
                                 'qtrim=r',
                                 'trimq=8'],
                                stderr=subprocess.PIPE,
                                universal_newlines=True)

    bbduk_stderr = bbduk_proc.stderr.split('Version')[1].splitlines()
    mlog.log('Version ' + bbduk_stderr[0],
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)
    for line in bbduk_stderr[1:]:
        mlog.log(line,
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # verify the output of the adapter trimming cmd
    if not file_check(r1_fastq_trimmed) or not file_check(r2_fastq_trimmed):
        mlog.log('bbduk failed to output adapter trimmed read file(s), aborting assembly',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False

    return True


def run_unicycler_assembly(r1_fastq_trimmed=None, r2_fastq_trimmed=None, long_read_file=None, mode='short',
                           individual_assembly_directory=None, threads='1', colors=1, stdout_verbosity_level=1,
                           log_file_verbosity_level=1, log_file=None):
    """
    run assembly using Unicycler.
    """

    # prepare the Unicycler command
    if mode == 'short':
        unicycler_command = 'unicycler --short1 ' + str(r1_fastq_trimmed) + ' --short2 ' + str(r2_fastq_trimmed) + \
                            ' --out ' + str(individual_assembly_directory) + ' --verbosity 1 '
    elif mode == 'long':
        unicycler_command = 'unicycler --short1 ' + str(r1_fastq_trimmed) + ' --short2 ' + str(r2_fastq_trimmed) + \
                            '--long' + str(long_read_file) + ' --out ' + str(individual_assembly_directory) +\
                            ' --verbosity 1 '

    # run Unicycler command
    if mode == 'short':
        subprocess.run(['unicycler',
                        '--short1', str(r1_fastq_trimmed),
                        '--short2', str(r2_fastq_trimmed),
                        '--out', str(individual_assembly_directory),
                        '--threads', threads,
                        '--verbosity', str(stdout_verbosity_level),
                        '--keep', '3'])
    elif mode == 'long':
        subprocess.run(['unicycler',
                        '--short1', str(r1_fastq_trimmed),
                        '--short2', str(r2_fastq_trimmed),
                        '--long', str(long_read_file),
                        '--out', str(individual_assembly_directory),
                        '--threads', threads,
                        '--verbosity', str(stdout_verbosity_level),
                        '--keep', '3'])


def assembly_file_formatting(assembly_file=None, sample_name=None, colors=1, stdout_verbosity_level=1,
                             log_file_verbosity_level=1, log_file=None):
    """
    The default unicycler assembly output contains a file "assembly.fasta" which is a multi-fasta file containing all
    of the assembled contigs. By default, each of the contig id/description lines is of the format:
        >[contig #] length=[contig length] depth=[relative depth]x
    We want to update the [contig #] field to fit into later aspects of our pipeline, so we will append the sample_name
    and contig_ with leading zeros to the output.

    We will write the reformatted contig name/descriptions to a new file in the same directory called
    [sample_name]_assembly.fasta

    :param assembly_file: POSIX path to the assembly file (fasta file output of assembler) to be reformatted
    :param sample_name: Name of the sample that was assembled
    :return: Posix path of the reformatted file if renaming was successful, the original path if other
    """

    # validate that there is a file at the assembly_file location, and if so prepare the reformatted file path
    if not assembly_file:
        mlog.log('No assembly file was provided!',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return assembly_file

    if not assembly_file.exists():
        mlog.log('Could not locate the assembly file at the specified path: ' + assembly_file,
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return assembly_file

    reformatted_assembly_file = assembly_file.parent / (sample_name + '_assembly.fasta')

    if reformatted_assembly_file.exists():
        mlog.log('The reformatted assembly file was located, so no reformatting will be performed\n',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return reformatted_assembly_file

    # read in all of the contig information from assembly_file using SeqIO
    mlog.log('Reformatting the assembly file now...',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)
    with open(assembly_file, 'r') as original, open(reformatted_assembly_file, 'w') as reformatted:
        contigs = SeqIO.parse(assembly_file, 'fasta')
        for contig in contigs:
            contig_id_element_list = contig.description.split(' ')
            contig_id_element_list[0] = sample_name + '_contig' + \
                                                 str(contig_id_element_list[0]).zfill(4)
            contig.id = contig_id_element_list[0]
            contig.description = ' '.join(contig_id_element_list[1:])
            SeqIO.write(contig, reformatted, 'fasta')

    mlog.log('Assembly file reformatting complete!',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    return reformatted_assembly_file


def filter_long_reads(r1_fastq=None, r2_fastq=None, raw_long_reads=None, processed_long_reads=None, colors=1,
                      stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None, force=False):
    """
    filtlong will be run with the following settings:
        min_length=10,000
        target_bases=500,000,000
        trim
        split=500
    """

    mlog.log_section_header('Long Read Data Trimming',
                            colors=colors,
                            stdout_verbosity_level=stdout_verbosity_level,
                            log_file_verbosity_level=log_file_verbosity_level,
                            log_file=log_file)
    mlog.log_explanation('Use filtlong to perform quality and length filtering of the provided long read sequencing '
                         'data',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)

    # check to see that filtlong is available on the users PATH
    if not check_for_dependency('filtlong'):
        mlog.log('Could not find filtlong on your PATH, so the long reads will not be trimmed!',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False
    else:
        mlog.log('utility located: filtlong',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # validate that the input requirements are met
    if not r1_fastq or not r2_fastq or not raw_long_reads:
        mlog.log('One or more of the required input files could not be located, so the long reads will not be trimmed!',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False

    # check for preexisting adapter trimmed files
    if file_check(processed_long_reads):
        if force:
            subprocess.run(['rm', str(processed_long_reads)])
        else:
            mlog.log('trimmed long read file located, so skipping trimming with filtlong',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            return True

    # log the filtlong command line input
    filtlong_command = "filtlong -1 " + str(r1_fastq)+ " -2 " + r2_fastq + " --min_length 10000 --target_bases " \
                       "500000000 --trim --split 500 " + raw_long_reads + " > " + str(processed_long_reads)

    mlog.log('Command: ' + mlog.bold(filtlong_command) + '\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    filtlong_proc = subprocess.run(['filtlong',
                                    '-1', str(r1_fastq),
                                    '-2', str(r2_fastq),
                                    '--min_length', '10000',
                                    '--target_bases', '500000000',
                                    '--trim',
                                    '--split', '500',
                                    str(raw_long_reads),
                                    '>', str(processed_long_reads)],
                                   shell=True,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True)

    return True


def assembly_QC(r1_fastq_trimmed=None, r2_fastq_trimmed=None, long_read_file=None, mode='short', output_directory=None,
                assembly=None, qc_directory=None, threads='1', colors=1, stdout_verbosity_level=1,
                log_file_verbosity_level=1, log_file=None):

    mlog.log_section_header('Assembly QC',
                            colors=colors,
                            stdout_verbosity_level=stdout_verbosity_level,
                            log_file_verbosity_level=log_file_verbosity_level,
                            log_file=log_file)
    mlog.log_explanation('Use QUAST to perform QC analysis of the assembly generated by unicycler',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)

    # check to see that QUAST is available on the users PATH
    if not check_for_dependency('quast'):
        mlog.log('Could not find quast on your PATH, so assembly QC can not be performed!',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False
    else:
        mlog.log('utility located: quast',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # ensure that all of the necessary file paths have been provided and are valid
    if not r1_fastq_trimmed or not r2_fastq_trimmed or not assembly:
        mlog.log('Not all of the requisite files were provided for assembly QC!',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False

    if not file_check(r1_fastq_trimmed) or not file_check(r2_fastq_trimmed) or not file_check(assembly):
        mlog.log('One or more of the specified input files could not be located at the provided location!',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False

    # if the mode is set to 'long', verify that the long read file path has been provided and is valid
    if mode == 'long':
        if not long_read_file:
            mlog.log('The path to the long read file was not provided, but the assembly QC request type was set to long'
                     '. Since the short reads and the assembly file were provided, we will use these to perform the '
                     'assembly QC.',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            mode = 'short'

        if not file_check(long_read_file):
            mlog.log('The path to the long read file provided is invalid, but the assembly QC request type was set to '
                     'long. Since the short reads and the assembly file were provided, we will use these to perform the'
                     ' assembly QC.',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            mode = 'short'

    # check to see if a qc_directory was specified. If so we will need to make sure that it doesn't already exist. If it
    # already exists or the user didn't specify a directory, we will default to a directory labelled "QC" in the output
    # directory if the output directory is specified or the parent of the assembly file is not.
    if qc_directory:
        if Path(qc_directory).expanduser().resolve().exists():
            mlog.log('The path provided for the QC directory already exists! Rather than overwrite it, we will '
                     'substitute the default QC directory.',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            qc_directory = None

    if not qc_directory:
        if output_directory:
            if file_check(output_directory):
                qc_directory = Path(output_directory).expanduser().resolve() / 'QC'
        else:
            qc_directory = Path(assembly).expanduser().resolve().parent / 'QC'

    # Log the quast command based on the mode (i.e. whether or not to include the long read data)
    if mode == 'short':
        quast_cmd = 'quast --min-contig 200 --threads ' + str(threads) + ' --pe1 ' + str(r1_fastq_trimmed) + ' --pe2 ' \
                    + str(r2_fastq_trimmed) + ' -o ' + str(qc_directory) + ' ' + str(assembly)
    elif mode == 'long':
        quast_cmd = 'quast --min-contig 200 --threads ' + str(threads) + ' --pe1 ' + str(r1_fastq_trimmed) + ' --pe2 ' \
                    + str(r2_fastq_trimmed) + ' --pacbio ' + str(long_read_file) + ' -o ' + str(qc_directory) + ' ' + \
                    str(assembly)

    mlog.log('Command: ' + mlog.bold(quast_cmd) + '\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    # run the quast command
    subprocess.run(quast_cmd, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)



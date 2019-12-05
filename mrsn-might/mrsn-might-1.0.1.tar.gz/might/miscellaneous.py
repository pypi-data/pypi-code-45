#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
from contextlib import redirect_stderr, redirect_stdout, contextmanager
from filecmp import dircmp
from pathlib import Path
import sys
import csv
import distutils.spawn
import subprocess
import time
import might_log as mlog



def file_check(file_path):
    """
    checks to see if the file associated with the individual_sequencing_sample object exists in the file system at the
    specified PATH. Returns True if yes and False if no. Also return False if the attribute does not exist
    """
    if Path(str(file_path)).expanduser().resolve().exists():
        return True
    else:
        return False


def check_for_dependency(program):
    """
    check_for_dependency() will use distutils.spawn to determine if the input dependency is available on the users PATH
    returns True if the dependency is located, False otherwise
    """
    if distutils.spawn.find_executable(str(program)):
        return True
    else:
        return False


def quit_with_error(message):
    """
    Displays the given message and ends the program's execution.
    """
    mlog.log('Error: ' + message, 0, stderr=True)
    sys.exit(1)


def compression_handler(sample, compress_or_decompress, list_of_attributes):
    """
    method handles the compression (gzip) or decompression (gunzip) of files
    """
    # If 'decompress' is requested, check compression state and decompress if necessary
    if compress_or_decompress == 'decompress':
        for attribute in list_of_attributes:
            file_path = str(getattr(sample, attribute))
            if file_path.endswith(".gz"):
                mlog.log('Extracting: ' + mlog.bold(file_path))
                subprocess.run(['gunzip', file_path])
                setattr(sample, attribute, Path(file_path[:-3]))
    # If 'compress' is requested, check compression state and compress if necessary
    if compress_or_decompress == 'compress':
        for attribute in list_of_attributes:
            file_path = str(getattr(sample, attribute))
            if not file_path.endswith(".gz"):
                mlog.log('Compressing: ' + mlog.bold(file_path))
                subprocess.run(['gzip', file_path])
                setattr(sample, attribute, Path(file_path + '.gz'))

    return


def parse_arguments(allmight=False, might=False):
    """
    capture user instructions from CLI. Based on the input provided, initialize an analysis
    """

    # parse user input
    parser = argparse.ArgumentParser(description='MIGHT! MRSN Integrated Genome Handling Tool \n', add_help=False)

    # Required arguments for a given sample. Need to know where to store the results (--output) and the name of the
    # sample (--sample_name)
    required_args = parser.add_argument_group('Required arguments')
    required_args.add_argument('--output',
                               type=str,
                               required=True,
                               help='path to the directory where output is/will be stored')

    # If parse_arguments is being called by the wrapper script AllMight.py, we will include the optional bcl2fastq
    # handling arguments
    if allmight:
        bcl2fastq_args = parser.add_argument_group('bcl2fastq2 arguments')
        bcl2fastq_args.add_argument('--bcl2fastq',
                                    action='store_true',
                                    help='Run bcl2fastq2 to generate demultiplexed fastq files from the bcl files')
        bcl2fastq_args.add_argument('--run-directory',
                                    type=str,
                                    default=None,
                                    help='Path to the run directory to be analyzed')
        bcl2fastq_args.add_argument('--sample-sheet',
                                    type=str,
                                    default=None,
                                    help='Path to the Illumina sample sheet file for the run being analyzed')

    # If parse_arguments is being called by the the individual sample handler Might.py, we will include the optional
    # path handling arguments used to tell the script where to find read/assembly files
    if might:
        input_args = parser.add_argument_group('Input arguments')
        input_args.add_argument('--sample-name',
                                type=str,
                                default=None,
                                help='Name of the sample to be analyzed.')
        input_args.add_argument('--fastq',
                                type=str,
                                help='path to the directory containing the read files for this sample '
                                     '[output/reads/raw_reads]')
        input_args.add_argument('--fasta',
                                type=str,
                                default=None,
                                help='path to the directory containing the assembly file for this sample '
                                     '[output/assembly]')
        input_args.add_argument('--long-reads',
                                type=str,
                                default=None,
                                help='path to the long reads file for this assembly')

    # Analysis arguments governing which analyses are going to be run on this sample.
    analysis_args = parser.add_argument_group('Analysis arguments')
    analysis_args.add_argument('--all',
                               action='store_true',
                               help='run all analysis options')
    analysis_args.add_argument('--kraken2',
                               action='store_true',
                               help='run Kraken2 on read files to determine species ID and potentially detect '
                                    'contamination')
    analysis_args.add_argument('--assembly',
                               action='store_true',
                               help='trim and filter reads using bbduk, then perform assembly using Unicycler')
    analysis_args.add_argument('--amr',
                               choices=['combination', 'reads', 'contigs', 'summary'],
                               help='run Andale using one of the four setting choices')
    analysis_args.add_argument('--mlst',
                               action='store_true',
                               help='perform MLST assignments for samples using MLST')
    analysis_args.add_argument('--plasmidfinder',
                               action='store_true',
                               help='run Plasmidfinder on contig files to identify rep gene content')

    # Resource arguments that provide the script with paths to databases and files required for some analysis steps
    resource_args = parser.add_argument_group('Resource arguments')
    resource_args.add_argument('--kraken2-database',
                               type=str,
                               default=None,
                               help='Path to the kraken2 database. Required for kraken2 analysis')
    resource_args.add_argument('--adapter-file',
                               type=str,
                               default=None,
                               help='Path to the adapter.fa file required for adapter trimming of Illumina reads')
    resource_args.add_argument('--ramdisk',
                               type=str,
                               help='Path to the ramdisk for speeding up kraken2')

    # Optional arguments that modify how the analysis steps are performed
    optional_args = parser.add_argument_group('Optional arguments')
    optional_args.add_argument('--update',
                               action='store_true',
                               help='update AMRFinderPlus and MLST databases')
    optional_args.add_argument('--force',
                               action='store_true',
                               help='force overwrite of existing data/output related to this sample')
    optional_args.add_argument('--cores',
                               type=int,
                               default=1,
                               help='the MAXIMUM number of CPUs to use in the analysis [1]')
    optional_args.add_argument('--verbosity',
                               type=int,
                               default=1,
                               help='the level of reporting done to the terminal window [1]')

    # Help and version arguments
    help_args = parser.add_argument_group('Help')
    help_args.add_argument('-h',
                           '--help',
                           action='help',
                           default=argparse.SUPPRESS,
                           help='show this help message and exit \n')

    # collect the user arguments
    args = parser.parse_args()

    # validate that no conflicting input was provided

    # bcl2fastq2 by definition does NOT run on single samples. In order for a bcl2fastq2 to run, a sample sheet
    # must have been provided, as well as a run directory. Missing either is fatal
    if allmight:
        if args.bcl2fastq:
            if not args.run_directory:
                quit_with_error('User requested bcl2fastq2 be performed, but failed to specify the path to the Illumina'
                                ' run output directory.\n Please ensure that the full path to the Illumina run output '
                                'directory is provided using --run-directory in the future!')
            if not Path(args.run_directory).expanduser().resolve().is_dir():
                quit_with_error('User requested bcl2fastq2 be performed, but the path to the Illumina run output '
                                'directory provided by the user cannot be located.\n Please ensure that the path to the'
                                ' Illumina run output directory provided using --run-directory is correct!')
            if not args.sample_sheet:
                quit_with_error('User requested bcl2fastq2 be performed, but failed to specify the path to the '
                                'SampleSheet.csv file.\n Please ensure that the full path to the SampleSheet.csv file '
                                'is provided using --sample-sheet in the future!')
            if not Path(args.sample_sheet).expanduser().resolve().exists():
                quit_with_error('User requested bcl2fastq2 be performed, but the path provided to the SampleSheet.csv '
                                'file can not be verified.\n Please ensure that the path to the SampleSheet.csv file '
                                'provided using --sample-sheet is correct!')
        # validate the formatting of the SampleSheet.csv file before proceeding
        args.sample_list, args.sample_sheet = validate_sample_sheet(samplesheet=args.sample_sheet,
                                                                    run_directory=args.run_directory)

    # if --all was selected, set the values of all analysis flags to true
    if args.all == True:
        args.bcl2fastq = True
        args.kraken2 = True
        args.assembly = True
        args.amr = True
        #args.mlst = True
        #args.plasmidfinder = True

    # if kraken2 analysis was requested but no kraken2_database was specified, quit with error message
    if args.kraken2 and not args.kraken2_database:
        quit_with_error('User requested kraken2 analysis but failed to provide a kraken2_database path.\nPlease ensure'
                        'that the full path to the prepared kraken2 database is provided using --kraken2_database in '
                        'the future!')

    # if assembly analysis is requested but no adapter.fa file path is specified, quit with error message
    if args.assembly:
        if not args.adapter_file:
            quit_with_error('User requested an assembly but failed to provide the path to the adapter.fa file '
                            'required to perform adapter trimming of the Illumina read files.\nPlease ensure that the '
                            'full path to the adapter.fa file is provided using --adapter_file in the future!')
        if not Path(args.adapter_file).expanduser().resolve().exists():
            quit_with_error('User requested an assembly but the path to the adapter.fa file required to perform adapter'
                            ' trimming of the Illumina read files can not be resolved. \nPlease ensure that the full '
                            'path to the adapter.fa file provided using --adapter_file is correct!')
        if might:
            if args.fasta:
                quit_with_error('User requested assembly be performed, but also provided the path to an assembly file. '
                                'Please provide EITHER --fasta OR --assembly in the future!')

    # validate the number of cores specified by the user.
    if args.cores < 0:
        quit_with_error('User requested a negative number of CPUs.')
    if args.cores > len(os.sched_getaffinity(0)):
        quit_with_error('User requested more cores for this analysis than are currently available.\nThe number of'
                        ' currently available cores is: ' + str(len(os.sched_getaffinity(0))))

    return args


def validate_sample_sheet(samplesheet=None, run_directory=None):
    """
     This method will make sure that:
         1)  the path to the sample sheet is valid
         2)  the sample sheet has the proper name (SampleSheet.csv) that bcl2fastq2 will accept
         3)  the sample sheet is free of duplicate sample names and/or barcode combinations
     Method will return a list of sample names
     """
    # sanitize input
    samplesheet = Path(samplesheet).expanduser().resolve()
    run_directory = Path(run_directory).expanduser().resolve()

    # determine if the run_directory can be located at the provided path
    if not run_directory.is_dir():
        quit_with_error('User requested bcl2fastq2 be performed, but the path to the Illumina run output directory '
                        'provided by the user cannot be located.\n Please ensure that the path to the Illumina run '
                        'output directory provided using --run-directory is correct!')

    # determine if the sample_sheet_file can be located at the provided path
    if not samplesheet.exists():
        quit_with_error('User requested bcl2fastq2 be performed, but the path provided to the SampleSheet.csv file'
                        'can not be verified.\n Please ensure that the path to the SampleSheet.csv file provided '
                        'using --sample-sheet is correct!')

    # verify that the sample sheet has the proper name that bcl2fastq2 will accept
    if not samplesheet.name == 'SampleSheet.csv':
        quit_with_error('The sample sheet provided by the user has an unacceptable name. bcl2fastq2 requires that the'
                        'sample sheet name be SampleSheet.csv (case sensitive!)')

    # verify that the sample sheet meets the no duplicates criteria for samples and barcode sets that will cause it to
    # fail silently
    sample_sheet_data = {}
    sample_list = []

    with open(str(samplesheet), 'r') as sample_sheet:
        sample_sheet_reader = csv.DictReader(sample_sheet,
                                             fieldnames=['Sample_ID', '', '', '', '', 'index', '', 'index2'],
                                             delimiter=',')
        sample_number = 0
        for row in sample_sheet_reader:
            if len(row['index']) == len(row['index2']) and len(row['index']) == 8:
                concatenated_indices = row['index'] + row['index2']
                sample_number += 1
                if row['Sample_ID'] in sample_sheet_data.keys():
                    quit_with_error('Duplicate sample names detected in the provided sample sheet: ' + row['Sample_ID'])
                elif concatenated_indices in sample_sheet_data.values():
                    quit_with_error('Duplicate barcode combinations detected in the provided sample sheet: I7=' +
                                    row['index'] + ' I5=' + row['index2'])
                else:
                    sample_sheet_data[row['Sample_ID']] = concatenated_indices
                    sample_list.append(row['Sample_ID'])

    # make sure that the SampleSheet.csv file is in the top level Illumina run directory, as that is where bcl2fastq
    # will be looking for it
    if samplesheet.parent == run_directory:
        return sample_list, samplesheet

    # since the SampleSheet.csv is not in the proper directory, we will copy it there
    copied_samplesheet = run_directory / samplesheet.name
    subprocess.run(['cp', str(samplesheet), str(copied_samplesheet)])

    # verify the copy took place
    if not copied_samplesheet.exists():
        quit_with_error('The sample sheet failed to move to the run directory.')

    return sample_list, copied_samplesheet


def query_yes_no(question, default=None):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def round_down(num, divisor):
    return num - (num % divisor)


@contextmanager
def suppress_stdout_stderr():
    """
    A context manager that temporarily directs stdout and stderr to devnull
    """
    with open (os.devnull,'w') as fnull:
        with redirect_stdout(fnull) as out, redirect_stderr(fnull) as err:
            yield (err, out)


def ramdisk_handler(mount=False, unmount=False, ramdisk_directory=None, directory_to_load=None, colors=1,
                    stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None):
    """
    RAMDISK. RAMDISK.

    All hail the SPPPEEEEEEEED.

    This method will attempt to mount or unmount a ramdisk for use in speeding up various aspects of the the selected
    analyses.

    :param mount: if mount is True, we will attempt to mount the ramdisk
    :param unmount: if unmount is True, we will attempt to unmount the ramdisk
    :param ramdisk_directory: if a path is provided, we will verify it exists and use it
    :param directory_to_load:  if a path is provided, we will verify it exists and use it
    :return: True if the requested action was accomplished (mount or unmount), False if not
    """

    if (mount and (not ramdisk_directory or not directory_to_load)) or (unmount and not ramdisk_directory):
        return False

    mlog.log('Checking the current status of the ramdisk\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    # verify that either mount or unmount are true (otherwise return False for impossible request)
    if (mount and unmount) or (not mount and not unmount):
        return False

    # verify that the ramdisk directory exists
    if ramdisk_directory:
        ramdisk_directory = Path(ramdisk_directory).expanduser().resolve()
        if not ramdisk_directory.is_dir():
            mlog.log('Unable to locate the ramdisk directory at the specified path',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            return False

    # verify that the directory_to_load exists
    if directory_to_load:
        directory_to_load = Path(directory_to_load).expanduser().resolve()
        if not directory_to_load.is_dir():
            mlog.log('Unable to locate the database directory at the specified path',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            return False

    # verify whether or not the ramdisk is mounted currently. This is accomplished by running
    # 'df -h | grep [ramisk_directory]' and capturing the stdout from the terminal. If the ramdisk is mounted the length
    # of the stdout and by extension mount_status will be non-zero.
    df_proc = str(subprocess.run(['df', '-h'], stdout=subprocess.PIPE).stdout)
    if str(ramdisk_directory) in df_proc:
        mlog.log('The ramdisk is currently mounted\n',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        mount_status = True
    else:
        mount_status = False

    # if mount was requested, handle the mounting and loading of the ramdisk as necessary
    if mount:

        # mount the ramdisk is it is not currently mounted
        if not mount_status:
            mlog.log('The ramdisk is not currently mounted. Mounting now...',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            # mount the ramdisk
            subprocess.run(['mount', str(ramdisk_directory)])
            # use the mount_status method above to verify successful mounting
            df_proc = str(subprocess.run(['df', '-h'], stdout=subprocess.PIPE).stdout)
            if str(ramdisk_directory) in df_proc:
                mlog.log('The ramdisk has been successfully mounted!\n',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
            else:
                mlog.log('Unable to mount the ramdisk',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
                return False

        # check to see if the database directory is currently mounted
        mlog.log('Checking to see if the database directory has already been loaded on to the ramdisk...',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        mounted_directory = ramdisk_directory / directory_to_load.name
        if mounted_directory.exists():
            # There are two possible scenarios where MIGHT might find that the database is already present on the
            # ramdisk. Possibility #1: Another application has already loaded the required files onto the ramdisk
            # completely. In this case we can just use it. Possibility #2: Another application IS IN THE PROCESS of
            # loading the required files. In this case we will sleep for 30s and then check again to see if the files
            # are fully loaded
            waiting_to_load = True
            while waiting_to_load:
                dcmp = dircmp(str(mounted_directory), str(directory_to_load))
                # Possibility #1: Another application has already loaded the required files onto the ramdisk
                if len(dcmp.right_only) == 0 and len(dcmp.left_only) == 0 and len(dcmp.diff_files) == 0:
                    mlog.log('The ramdisk is mounted, the database is loaded, time to boogie!\n',
                             colors=colors,
                             stdout_verbosity_level=stdout_verbosity_level,
                             log_file_verbosity_level=log_file_verbosity_level,
                             log_file=log_file)
                    return True
                # Possibility  # 2: Another application IS IN THE PROCESS of loading the required files. In this case
                # we will sleep for 30s and then check again to see if the files are fully loaded
                else:
                    mlog.log('The ramdisk is currently being loaded by another application. Waiting...!\n',
                             colors=colors,
                             stdout_verbosity_level=stdout_verbosity_level,
                             log_file_verbosity_level=log_file_verbosity_level,
                             log_file=log_file)
                    time.sleep(30)

        # load the database directory on to the ramdisk
        mlog.log('Database directory has NOT been loaded to the ramdisk.\n',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        mlog.log('Copying the database directory contents to the ramdisk...',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        subprocess.run(['cp', '-r', str(directory_to_load), str(ramdisk_directory)])

        time.sleep(1)

        # verify that the directory was loaded successfully
        dcmp = dircmp(str(mounted_directory), str(directory_to_load))
        if len(dcmp.right_only) > 0:
            mlog.log('The ramdisk failed to load the full complement of files from the database directory',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            return False
        if len(dcmp.diff_files) > 0:
            mlog.log('Discrepancies exist between the files in the database directory and the ramdisk',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            return False

        mlog.log('Database directory successfully loaded to ramdisk. Ready for use!\n',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return True

    # if unmount was requested, handle the unmounting of the ramdisk
    if unmount:
        if mount_status:
            # umount the ramdisk
            mlog.log('Unmounting the ramdisk...\n',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)
            subprocess.run(['umount', str(ramdisk_directory)])

            # verify that the unmount was successful
            df_proc = str(subprocess.run(['df', '-h'], stdout=subprocess.PIPE).stdout)
            if str(ramdisk_directory) in df_proc:
                mlog.log('Unmounting failed!\n',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
            else:
                mlog.log('Unmounting complete!\n',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
        return True


def ascii_art(logo=None):
    """
    Print out the ascii art logo requested by the user
    :param logo: the name of the logo to be printed
    """

    if logo =='andale':
        print(mlog.bold_green("""

               ___               _              _
              /   \   _ _     __| |    __ _    | |     ___
              | - |  | ' \   / _` |   / _` |   | |    / -_)
              |_|_|  |_||_|  \__,_|   \__,_|  _|_|_   \___|
            _|=====|_|====|_|======|_|=====|_|=====|_|=====|
            "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'

        """))

    if logo =='might':
        print(mlog.bold_green("""
        
        
            .___  ___.  __    _______  __    __  .__________.
            |   \/   | |  |  /  _____||  |  |  | |          |
            |  \  /  | |  | |  |  __  |  |__|  | `---|  |---`
            |  |\/|  | |  | |  | |_ | |   __   |     |  |     
            |  |  |  | |  | |  |__| | |  |  |  |     |  |     
            |__|  |__| |__|  \______| |__|  |__|     |__|     
    
                
        """))

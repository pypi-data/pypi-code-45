#!/usr/bin/env python
# encoding: utf-8

import subprocess

import might_log as mlog
from miscellaneous import check_for_dependency, file_check, ramdisk_handler


def kraken2_precheck(kraken2_database=None, force=False, kraken2_directory=None, kraken2_report=None, r1_fastq=None,
                     r2_fastq=None, colors=1, stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None):
    """
    sets all of the file/directory path attributes associated with a kraken2 analysis. If the kraken2_database value
    is NOT provided then the analysis will be aborted. If the ramdisk value is provided, set the attributes
    necessary for running kraken2 with --memory-mapping
    """

    if not check_for_dependency('kraken2'):
        mlog.log('Could not find kraken2 on your PATH, so this analysis is being aborted',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False

    if not file_check(r1_fastq) or not file_check(r2_fastq):
        mlog.log('Could not find both read files, so this analysis is being aborted',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False

    if not kraken2_database:
        mlog.log('The path to the kraken2 database was not provided, so this analysis is being aborted',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False

    # verify that the kraken2_database path provided is valid
    if not file_check(kraken2_database):
        mlog.log('The path to the kraken2 database appears to be invalid, so this analysis is being aborted',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return False

    # check to see if the kraken2_directory exists already. If so, check to see if the output kraken2_report is already
    # present. If not, make the directory
    if file_check(kraken2_directory):
        if file_check(kraken2_report):
            if force:
                mlog.log('Kraken2 output for this sample was already present, but --force was invoked so we will '
                         'overwrite the existing results',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
                subprocess.run(['rm', str(kraken2_report)])
            else:
                mlog.log('Kraken2 output for this sample was already present, so this analysis is being aborted',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
                return False
    else:
        mlog.log('Preparing the kraken2 output directory...\n',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        if not file_check(str(kraken2_directory)):
            subprocess.run(['mkdir', str(kraken2_directory)])

    return True


def run_kraken2(kraken2_database=None, kraken2_report=None, r1_fastq=None, r2_fastq=None, ramdisk=None, threads='1',
                colors=1, stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None):
    """
    run kraken2
    """

    if ramdisk_handler(mount=True,
                       ramdisk_directory=ramdisk,
                       directory_to_load=kraken2_database,
                       colors=colors,
                       stdout_verbosity_level=stdout_verbosity_level,
                       log_file_verbosity_level=log_file_verbosity_level,
                       log_file=log_file):

        # run kraken2 command with ramdisk utility
        kraken2_cmd = 'kraken2 --db ' + str(ramdisk / kraken2_database.name) + ' --memory-mapping --use-names --report '\
                      + str(kraken2_report) + \
                      ' --threads ' + threads + ' --paired  ' + str(r1_fastq) + ' ' + str(r2_fastq)
        mlog.log('Command: ' + mlog.bold(kraken2_cmd),
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        mlog.log('Now running kraken2...\n',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        kraken2_process = subprocess.run(['kraken2',
                                          '--db', str(ramdisk / kraken2_database.name),
                                          '--memory-mapping',
                                          '--use-names',
                                          '--report', str(kraken2_report),
                                          '--threads', threads,
                                          '--paired', str(r1_fastq), str(r2_fastq)],
                                         stdout=subprocess.DEVNULL,
                                         stderr=subprocess.PIPE,
                                         universal_newlines=True)
        mlog.log(str(kraken2_process.stderr),
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
    else:
        # run kraken2 command without ramdisk utility

        kraken2_cmd = 'kraken2 --db  ' + str(kraken2_database) + ' --use-names --report  ' + str(kraken2_report) + \
                      ' --threads 1 --paired  ' + str(r1_fastq) + ' ' + str(r2_fastq)
        mlog.log('Command: ' + mlog.bold(kraken2_cmd),
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        mlog.log('Now running kraken2...\n',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        kraken2_process = subprocess.run(['kraken2',
                                          '--db', str(kraken2_database),
                                          '--use-names',
                                          '--report', str(kraken2_report),
                                          '--threads', threads,
                                          '--paired', str(r1_fastq), str(r2_fastq)],
                                         stdout=subprocess.DEVNULL,
                                         stderr=subprocess.PIPE,
                                         universal_newlines=True)
        mlog.log(str(kraken2_process.stderr),
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # validate that an output file was generated, and update sample.kraken2_status accordingly
    if not file_check(kraken2_report):
        mlog.log('Kraken2 failed to produce a report. See log file for details',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    mlog.log('Kraken2 analysis is complete',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)
    return


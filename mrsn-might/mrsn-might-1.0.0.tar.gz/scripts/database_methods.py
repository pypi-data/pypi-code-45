#!/usr/bin/env python
# encoding: utf-8

import subprocess
from pathlib import Path
import Might_log as mlog
import time


def database_check(update=False, colors=1, stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None):
    """
    Check to see if we can see a) the AMRFinderPlus database and b) the ariba reference derived from (a)
    """

    mlog.log_section_header('AMR Database Validation',
                            colors=colors,
                            stdout_verbosity_level=stdout_verbosity_level,
                            log_file_verbosity_level=log_file_verbosity_level,
                            log_file=log_file)
    mlog.log_explanation('In order to perform AMR gene identification, Andale requires that a copy of the NCBI '
                         'AMRFinderPlus database is installed on your machine in an accessible location. Additionally, '
                         'a reference directory prepared using the AMR_CDS file by ARIBA is required to perform AMR '
                         'gene identification from read files.',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)

    mlog.log('Checking for the required databases...',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    # by default we will NOT remake the ARIBA reference unless we have to
    refresh = False

    # get the path of the directory where andale.py is installed. This is where the ariba reference will be stored
    conda_bin_directory = Path(__file__).resolve().parent

    # find the path to the amrfinder executable, as it installs its database relative to this location
    proc = subprocess.Popen(['which', 'amrfinder'], stdout=subprocess.PIPE)
    amrfinder_path = Path(str(proc.stdout.read().strip())[2:-1])
    amrfinder_database = amrfinder_path.parent.parent / 'share' / 'amrfinderplus' / 'data' / 'latest'
    amrfinder_database = Path(amrfinder_database).resolve()
    ariba_database = conda_bin_directory / 'andale_ariba_amrfinder_reference'

    # check for a lock file to see if another instance of MIGHT/Andale is attempting to prepare the database. If a lock
    # file is found, enter a while loop that checks periodically if the lock file has been removed, then proceed. If no
    # lock file is encountered, create one until all database preparation methods are complete

    database_lock_file = amrfinder_database.parent / 'andale.lock'

    while database_lock_file.exists():
        mlog.log('encountered database lock file. Waiting for permission to proceed',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        time.sleep(10)

    # check to see if the AMRFinderPlus database is present. If the AMRFinderPlus database directory can't be located,
    # call the get_amrfinderplus_database() method to download it

    if not amrfinder_database.is_dir() or update:
        get_amrfinderplus_database(database_lock_file,
                                   colors=colors,
                                   stdout_verbosity_level=stdout_verbosity_level,
                                   log_file_verbosity_level=log_file_verbosity_level,
                                   log_file=log_file)
        # if we are downloading a new AMRFinder database we will also want to remake the ariba reference if it already
        # exists
        if ariba_database.is_dir():
            refresh = True
    else:
        mlog.log('AMRFinderPlus database directory located',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # check to see if ariba prepareref has been run on the AMRFinderPlus database. If the ariba reference directory
    # can't be located or needs to be remade, call the prepare_ariba_reference() method to construct it
    if not ariba_database.is_dir() or refresh:
        prepare_ariba_reference(ariba_database,
                                amrfinder_database,
                                refresh,
                                colors=colors,
                                stdout_verbosity_level=stdout_verbosity_level,
                                log_file_verbosity_level=log_file_verbosity_level,
                                log_file=log_file)
    else:
        mlog.log('ARIBA reference directory located',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

    # remove lock file if it exists
    if database_lock_file.exists():
        subprocess.run(['rm', str(database_lock_file)])

    return amrfinder_database, ariba_database


def get_amrfinderplus_database(database_lock_file, colors=1, stdout_verbosity_level=1, log_file_verbosity_level=1,
                               log_file=None):
    """
    Download the latest version of the AMRFinderPlus database from the ncbi via rsync
    """
    subprocess.run(['touch', str(database_lock_file)])
    mlog.log('Downloading AMRFinderPlus database from NCBI...',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)
    # utilize the AMRFinderPlus built in utility to download/update the amrfinder database
    subprocess.run(['amrfinder', '--update'], stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)
    mlog.log('Download complete!\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)
    return


def prepare_ariba_reference(ariba_database, amrfinder_database, refresh, colors=1, stdout_verbosity_level=1,
                            log_file_verbosity_level=1, log_file=None):
    """
    Prepare the ariba reference directory using the AMRFinderPlus database
    """
    mlog.log('Preparing the ARIBA reference using the AMRFinderPlus database...\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    # if refresh is true we first need to remove the existing ariba reference directory
    if refresh:
        subprocess.run(['rm', '-r', ariba_database])

    # we require the 'AMR_CDS' file from the database to construct the ariba reference
    amrfinder_CDS_file = amrfinder_database / 'AMR_CDS'
    ariba_prepareref_cmd = 'ariba prepareref --all_coding yes -f ' + str(amrfinder_CDS_file) + ' ' + str(ariba_database)

    mlog.log('ARIBA prepareref command: '+ariba_prepareref_cmd,
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    subprocess.run(ariba_prepareref_cmd, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)

    mlog.log('ARIBA reference is ready for use!\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    return


if __name__ == '__main__':
    database_check()
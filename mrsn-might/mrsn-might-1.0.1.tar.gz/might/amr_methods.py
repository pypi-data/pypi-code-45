#!/usr/bin/env python
# encoding: utf-8

import csv
import os
import subprocess
import time
from pathlib import Path
import pandas as pd
from Bio import SeqIO
import might_log as mlog
from miscellaneous import compression_handler, suppress_stdout_stderr, file_check


def amr_precheck(r1_fastq=None, r2_fastq=None, assembly=None, individual_amr_directory=None, analysis_type=None,
                 force=False, colors=1, stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None):
    """
     sets all of the file/directory path attributes associated with an andale run. Analysis type is assigned by the
     user in the CLI, then validated by performing scan_for_fastq() and scan_for_assembly(),
    """
    """
    Determination of the type of andale analysis to run. There are 4 primary options: 
    --combination: reads using ARIBA and AMRFinderPlus on the ARIBA output and the contigs file
    --reads: reads only using ARIBA and AMRFinderPlus
    --contigs: AMRFinderPlus on the contigs file only
    --summary_only: which performs no new analysis but instead summarizes the preexisting data 
    """

    # if the user specifies that they want --summary_only, this will supersede any other requests
    if analysis_type == "summary":
        amr_analysis_type = "summary"
        return amr_analysis_type

    # for all other cases, we will use the user input (if it exists) and/or the presence/absence of the input

    # check to see if the AMR output is already present.
    if individual_amr_directory:
        if file_check(individual_amr_directory):
            if force:
                mlog.log('Andale output already exists for this sample, but --force was invoked so existing output will'
                         ' be overwritten\n',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
                subprocess.run(['rm', '-r', str(individual_amr_directory)])
            # else:
            #    log.log('Andale output for this sample was already present, so this analysis is being aborted\n')
            #    return None

    # case #1: all three input files are present
    if r1_fastq and r2_fastq:
        if assembly:
            if analysis_type == 'ARIBA only':
                mlog.log('Andale analysis type has been set to: reads only',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
                amr_analysis_type = 'reads'
            if analysis_type == 'contigs only':
                mlog.log('Andale analysis type has been set to: contigs only',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
                amr_analysis_type = 'contigs'
            else:
                mlog.log('Andale analysis type has been set to: combination',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)
                amr_analysis_type = 'combination'

    # case #2: only the read files are present
    if r1_fastq and r2_fastq and not assembly:
        mlog.log('Andale analysis type has been set to: reads only',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        amr_analysis_type = 'reads'

    # case #3: only the assembly file is present
    if (not r1_fastq or not r2_fastq) and assembly:
        mlog.log('Andale analysis type has been set to: contigs only',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        amr_analysis_type = 'contigs'

    # case #4: none of the requisite file types are present so no analysis can be performed
    if (not r1_fastq or not r2_fastq) and not assembly:
        mlog.log('Insuffcient files available for any AMR prediction, aborting this analysis',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return None

    return amr_analysis_type


def ariba_run(sample, colors=1, stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None):
    """
    This method will handle the ariba/ncbi run command for a single sample:
    1. Check/modify compression of read files
    2. Perform local assembly of the read files using ariba and the AMRFinderPlus-derived prepared reference database
    3. Compress the read files once ariba is done
    """

    mlog.log_section_header('ARIBA - AMR prediction from read files',
                            colors=colors,
                            stdout_verbosity_level=stdout_verbosity_level,
                            log_file_verbosity_level=log_file_verbosity_level,
                            log_file=log_file)
    mlog.log_explanation('ARIBA is used to assemble raw illumina reads to the AMRFinderPlus reference database prepared '
                        'during the AMR Database Validation step. While ARIBA offers its own built in prediction method'
                        ' (refer to /AMR/<sample name>/ARIBA_output/report.tsv), we will be using the assemblies.fa '
                        'file as input for AMRFinderPlus protein-based prediction',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)

    # check for checkpoint file
    checkpoint_file = sample.ariba_assemblies

    if file_check(checkpoint_file):
        mlog.log('CHECKPOINT DETECTED: ariba checkpoint file detected, skipping this analysis',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return True

    # decompress the R1 and R2 reads (if compressed)
    compression_handler(sample, 'decompress', ['r1_fastq', 'r2_fastq'])
    time.sleep(1)

    """
    ariba is prone to erroring out when running mutliple threads. Failure of the process is indictated by the message: "Stopping!
    Signal received: 28". We suspect this is a terminal error relating to timeout. In an effort to get around this, we will
    loop ariba until it completes without returning the error code with a maximum of 3 attempts
    """

    # run ariba, directing output files to sample.ariba_output_directory and piping the stderr to ariba_process
    ariba_cmd = 'ariba run ' + str(sample.ariba_database) + '/ ' + str(sample.r1_fastq) + ' ' + \
                str(sample.r2_fastq) + ' ' + str(sample.ariba_output_directory)

    mlog.log('Command: ' + mlog.bold(ariba_cmd) + '\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    error_code_received = True
    attempt_count = 0
    formatted_attempt_count = ['0', '1st', '2nd', '3rd']
    while error_code_received and attempt_count < 4:
        attempt_count += 1

        mlog.log('Running ARIBA...',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)

        ariba_process = subprocess.run(['ariba', 'run',
                                        str(sample.ariba_database),
                                        str(sample.r1_fastq),
                                        str(sample.r2_fastq),
                                        str(sample.ariba_output_directory),
                                        '--threads', sample.cores],
                                       stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

        # read in the stderr captured in ariba_process
        ariba_error = str(ariba_process.stderr)

        # check to see if the aborted run signal is present in ARIBA's stderr. If so, delete the failed ariba output
        # and try again
        if "Signal received: 28" in ariba_error:
            mlog.log('ariba runtime error encountered, resulting in run termination. Retrying for the ' +
                    formatted_attempt_count[attempt_count] + ' time',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)

            subprocess.run(['rm', '-r', sample.ariba_output_directory])
        else:
            error_code_received = False

            mlog.log('ARIBA run finished successfully',
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)

            return True

    return False


def amrfinderplus_run(sample, list_of_attributes, analysis_type, colors=1, stdout_verbosity_level=1,
                      log_file_verbosity_level=1, log_file=None):
    """
    run AMRFinderPlus on the selected sample object for the attribute (file) selected (contig file/ariba assemblies file)
    list_of_attributes is a two item list [input file for AMRFinderPlus, output file from AMRFinderPlus]
    """

    mlog.log_section_header('AMRFinderPlus - AMR prediction from assemblies for ' + analysis_type,
                            colors=colors,
                            stdout_verbosity_level=stdout_verbosity_level,
                            log_file_verbosity_level=log_file_verbosity_level,
                            log_file=log_file)
    mlog.log_explanation('AMRFinderPlus will be used to perform AMR prediction using the assemblies associated with'
                        ' ' + analysis_type + '.',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)

    output_file = str(getattr(sample, list_of_attributes[1]))

    # check for output file (checkpoint)
    if file_check(output_file):
        mlog.log('CHECKPOINT DETECTED: checkpoint file detected, skipping this analysis',
                 colors=colors,
                 stdout_verbosity_level=stdout_verbosity_level,
                 log_file_verbosity_level=log_file_verbosity_level,
                 log_file=log_file)
        return

    # decompress the input file, if required
    mlog.log('decompressing the input file (if necessary)\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)
    compression_handler(sample, 'decompress', [list_of_attributes[0]])
    time.sleep(2)

    input_file = str(getattr(sample, list_of_attributes[0]))

    # run amrfinder in nucleotide mode for assembled_genes.fa
    amrfinderplus_cmd = 'amrfinder --plus -d ' + str(sample.amrfinder_database) + ' -o ' + str(output_file) + ' -n ' +\
                        str(input_file) + ' --threads 1'

    mlog.log('Command: ' + mlog.bold(amrfinderplus_cmd) + '\n',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)
    mlog.log('Now running AMRFinder for ' + analysis_type,
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    subprocess.run(['amrfinder',
                    '--plus',
                    '-d', str(sample.amrfinder_database),
                    '-o', str(output_file),
                    '-n',
                    str(input_file),
                    '--threads', '1'],
                   stderr=subprocess.STDOUT,
                   stdout=subprocess.DEVNULL)

    # compress input file to save space
    mlog.log('AMRFinder finished for ' + analysis_type + '.',
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)
    compression_handler(sample, 'compress', [list_of_attributes[0]])

    return


def summarize_amr_finder_output(sample, colors=1, stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None):
    """
    summarize all of the amr_finder generated output for all of the samples into a single file, andale_summary.csv
    Merge all of the available AMRFinderPlus output derived from contigs, repeat the process for output based on ariba
    assemblies. Generate TWO integrated report files:
        1) andale_output_raw.csv, which is merely a concatenation of all available output for every sample, with true
           duplicates removed
        2) andale_output_FILTERED.csv, TBD
    """

    mlog.log_section_header('Summarize Results',
                            colors=colors,
                            stdout_verbosity_level=stdout_verbosity_level,
                            log_file_verbosity_level=log_file_verbosity_level,
                            log_file=log_file)
    mlog.log_explanation('Generate summary tables of all AMRFinderPlus results.',
                         colors=colors,
                         stdout_verbosity_level=stdout_verbosity_level,
                         log_file_verbosity_level=log_file_verbosity_level,
                         log_file=log_file)

    ariba_summary_file = sample.individual_amr_directory / 'ariba_summary.csv'
    contig_summary_file = sample.individual_amr_directory / 'contigs_summary.csv'
    andale_output_raw_file = sample.individual_amr_directory / 'andale_output_raw.csv'
    andale_output_filtered = sample.individual_amr_directory / 'andale_output_filtered.csv'

    # remove existing summary files is they are present
    for file in [ariba_summary_file, contig_summary_file, andale_output_raw_file, andale_output_filtered]:
        if Path(file).resolve().exists():
            subprocess.run(['rm', str(Path(file))])

    # Create DataFrame "andale_output_raw" which we will add all of the data generated during the analysis run to
    andale_output_raw = pd.DataFrame(
        columns=['sample', 'method', 'Gene symbol', 'Sequence name', 'Method', '% Coverage of reference sequence',
                 '% Identity to reference sequence', 'Start', 'Stop', 'Strand', 'Contig id',
                 'Accession of closest sequence', 'Name of closest sequence', 'Class', 'Subclass'])

    for source in ['ariba', 'Contigs']:

        if source == 'ariba':
            input_file = str(sample.amrfinder_output_from_ariba)
            summary_file = ariba_summary_file

        if source == 'Contigs':
            input_file = str(sample.amrfinder_output_from_contigs)
            summary_file = contig_summary_file
            if Path(input_file).exists():
                # v0.4 -- if contigs were used, add the total length of the contig the hit is located on to the output
                # csv(s)
                contig_lengths = get_contig_lengths(sample)

        if Path(input_file).exists():

            mlog.log('Generating summary file: ' + mlog.bold(input_file),
                     colors=colors,
                     stdout_verbosity_level=stdout_verbosity_level,
                     log_file_verbosity_level=log_file_verbosity_level,
                     log_file=log_file)

            input_column_list = ['Gene symbol', 'Sequence name', 'Scope', 'Element type', 'Element subtype',
                                 'Class', 'Subclass', 'Method', '% Coverage of reference sequence',
                                 '% Identity to reference sequence', 'Start', 'Stop', 'Strand', 'Contig id',
                                 'Accession of closest sequence', 'Name of closest sequence']
            output_column_list = ['sample', 'source', 'Gene symbol', 'Sequence name', 'Method',
                                  '% Coverage of reference sequence', '% Identity to reference sequence', 'Start',
                                  'Stop', 'Strand', 'Contig id', 'Contig length', 'Accession of closest sequence',
                                  'Name of closest sequence', 'Scope', 'Element type', 'Element subtype', 'Class',
                                  'Subclass']

            # Read in the current input file (either contig or ariba output) to the DataFrame "report_data"
            report_data = pd.read_csv(input_file, sep='\t', usecols=input_column_list)
            report_data['sample'] = sample.name
            report_data['source'] = source

            # v0.4 -- if contigs were used, add the total length of the contig the hit is located on to "report_data"
            if source == 'Contigs':
                report_data['Contig id'] = report_data['Contig id'].astype(str)
                report_data = report_data.merge(contig_lengths, on='Contig id', how='left')

            # add the current "report_data" to "andale_output_raw"
            andale_output_raw = pd.concat([andale_output_raw, report_data], ignore_index=True, sort=False)

            # v0.5 -- pandas to_csv passes a FutureWarning we don't need to see, so we'll redirect the terminal output
            # to devnull temporarily
            with suppress_stdout_stderr():

                # add all of the sample data for a given source (contigs or ariba) to the corresponding summary file
                if not os.path.isfile(summary_file):
                    report_data.to_csv(summary_file, sep=',', index=False, columns=output_column_list, mode='a')
                else:
                    report_data.to_csv(summary_file, sep=',', index=False, columns=output_column_list, mode='a',
                                       header=False)

    # Generate andale_output_raw.csv by concatenating ariba_summary.csv and contigs_summary.csv

    mlog.log('Generating summary file: ' + mlog.bold(str(andale_output_raw_file)),
             colors=colors,
             stdout_verbosity_level=stdout_verbosity_level,
             log_file_verbosity_level=log_file_verbosity_level,
             log_file=log_file)

    andale_output_raw.to_csv(andale_output_raw_file, sep=',', index=False, columns=output_column_list, mode='a')

    # Results filtering: Since we are potentially calling genes from two sources (assembled contigs and ARIBA output) we
    # anticipate that there will be significant redundancy in the output. In an attempt not to drive folks crazy with
    # deduplicating the resulting .csv file, we will perform some "safe" deduplication operations on the output
    # dataframe. Note that you still have access to the complete dataset in the andale_output_raw.csv file

    # First, we can safely drop all true duplicate entries from the dataframe
    andale_output_raw.drop_duplicates(inplace=True)

    # Second, in the case where the result for a given sample/gene is identical in the method of call (either EXACTX or
    # ALLELEX) as well as the %coverage and %ID, we will selectively keep the result from the contigs as this will
    # provide the greatest context
    filtered_andale_output = andale_output_raw.groupby(['sample', 'Gene symbol', 'Method',
                                                        '% Coverage of reference sequence',
                                                        '% Identity to reference sequence'])
    for name, group in filtered_andale_output:
        if len(group.index) > 1:
            if 'Contigs' in group.source.values:
                filter_methods = ['EXACTX', 'ALLELEX']
                filtered_group = group[((group['Method'].isin(filter_methods)) |
                                       ((group['Method'] == 'BLASTX') &
                                        (group['% Coverage of reference sequence'] >= 90) &
                                        (group['% Identity to reference sequence'] >= 90))) &
                                        (group['source'] == 'Contigs')]
                for i in group.index:
                    if i not in filtered_group.index:
                        andale_output_raw.drop(i, inplace=True)

    # Third, in the case where an EXACTX or ALLELEX hit OR a BLASTX hit with >95/95 %coverage/%ID exists for a given
    # sample/gene combination, we will remove any PARTIAL_CONTIG_ENDX or PARTIAL_CONTIGX that are the result of ARIBA
    # assembling partial genes adjacent to the target gene
    filtered_andale_output = andale_output_raw.groupby(['sample', 'Gene symbol'])
    for name, group in filtered_andale_output:
        if len(group.index) > 1:
            if ('PARTIAL_CONTIG_ENDX' in group.Method.values) or ('PARTIAL_CONTIGX' in group.Method.values):
                filter_methods = ['EXACTX', 'ALLELEX']
                filtered_group = group[(group['Method'].isin(filter_methods)) |
                                       ((group['Method'] == 'BLASTX') &
                                        (group['% Coverage of reference sequence'] >= 90) &
                                        (group['% Identity to reference sequence'] >= 90))]
                print(filtered_group.index)
                for i in group.index:
                    if i not in filtered_group.index:
                        andale_output_raw.drop(i, inplace=True)

    andale_output_raw.to_csv(andale_output_filtered, sep=',', index=False, columns=output_column_list, mode='a')

    return

def get_contig_lengths(sample):
    """
    method takes a multifasta file and returns a pandas series where the index is the name of the contigs
    and the values are the lengths of those contigs
    """

    compression_handler(sample, 'decompress', ['assembly_file'])

    # Use SeqIO to read all of the contig names and lists into two lists, contig_names and contig_lengths
    contig_length_dict = {'Contig id': [], 'Contig length': []}
    for contig in SeqIO.parse(sample.assembly_file, "fasta"):
        contig_length_dict['Contig id'].append((str(contig.id).split(' '))[0])
        contig_length_dict['Contig length'].append(int(len(contig.seq)))

    # convert the two lists into a series object
    contig_lengths = pd.DataFrame(contig_length_dict, columns=['Contig id', 'Contig length'])

    compression_handler(sample, 'compress', ['assembly_file'])

    return contig_lengths


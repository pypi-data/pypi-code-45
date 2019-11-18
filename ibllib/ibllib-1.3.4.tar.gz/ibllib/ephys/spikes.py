from pathlib import Path
import logging
import json

import numpy as np
from scipy.interpolate import interp1d

from phylib.io import alf

import ibllib.ephys.ephysqc as ephysqc
from ibllib.misc import log2session_static
from ibllib.io import spikeglx, raw_data_loaders
from ibllib.io.extractors.ephys_fpga import glob_ephys_files

_logger = logging.getLogger('ibllib')


@log2session_static('ephys')
def probes_description(ses_path):
    """
    Aggregate probes informatin into ALF files
        alf/probes.description.npy
        alf/probes.trajecory.npy
    """

    ses_path = Path(ses_path)
    ephys_files = glob_ephys_files(ses_path)
    subdirs, labels, efiles_sorted = zip(
        *sorted([(ep.ap.parent, ep.label, ep) for ep in ephys_files if ep.get('ap')]))

    """Ouputs the probes description file"""
    probe_description = []
    for label, ef in zip(labels, efiles_sorted):
        md = spikeglx.read_meta_data(ef.ap.with_suffix('.meta'))
        probe_description.append({'label': label,
                                  'model': md.neuropixelVersion,
                                  'serial': int(md.serial),
                                  'raw_file_name': md.fileName,
                                  })
    probe_description_file = ses_path.joinpath('alf', 'probes.description.json')
    with open(probe_description_file, 'w+') as fid:
        fid.write(json.dumps(probe_description))

    """Ouputs the probes trajectory file"""
    bpod_meta = raw_data_loaders.load_settings(ses_path)
    if not bpod_meta.get('PROBE_DATA'):
        _logger.error('No probe information in settings JSON. Skipping probes.trajectory')
        return

    def prb2alf(prb, label):
        return {'label': label, 'x': prb['X'], 'y': prb['Y'], 'z': prb['Z'], 'phi': prb['A'],
                'theta': prb['P'], 'depth': prb['D'], 'beta': prb['T']}

    # the labels may not match, in which case throw a warning and work in alphabetical order
    if labels != ['probe00', 'probe01']:
        _logger.warning("Probe names do not match the json settings files. Will match coordinates"
                        " per alphabetical order !")
        _ = [_logger.warning(f"  probe0{i} ----------  {lab} ") for i, lab in enumerate(labels)]
    trajs = []
    keys = sorted(bpod_meta['PROBE_DATA'].keys())
    for i, k in enumerate(keys):
        if i >= len(labels):
            break
        trajs.append(prb2alf(bpod_meta['PROBE_DATA']['probe00'], labels[i]))
    probe_trajectory_file = ses_path.joinpath('alf', 'probes.trajectory.json')
    with open(probe_trajectory_file, 'w+') as fid:
        fid.write(json.dumps(trajs))


@log2session_static('ephys')
def sync_spike_sortings(ses_path):
    """
    Converts the KS2 outputs for each probe in ALF format. Creates:
    alf/probeXX/spikes.*
    alf/probeXX/clusters.*
    alf/probeXX/templates.*
    :param ses_path: session containing probes to be merged
    :return: None
    """
    def _sr(ap_file):
        # gets sampling rate from data
        md = spikeglx.read_meta_data(ap_file.with_suffix('.meta'))
        return spikeglx._get_fs_from_meta(md)

    ses_path = Path(ses_path)
    ephys_files = glob_ephys_files(ses_path)
    subdirs, labels, efiles_sorted, srates = zip(
        *sorted([(ep.ap.parent, ep.label, ep, _sr(ep.ap)) for ep in ephys_files if ep.get('ap')]))

    _logger.info('converting  spike-sorting outputs to ALF')
    for subdir, label, ef, sr in zip(subdirs, labels, efiles_sorted, srates):
        probe_out_path = ses_path.joinpath('alf', label)
        # computes QC on the ks2 output
        ephysqc._spike_sorting_metrics_ks2(subdir, save=True)
        # converts the folder to ALF
        ks2_to_alf(subdir, probe_out_path, label=None, force=True)
        # synchronize the spike sorted times
        sync_file = ef.ap.parent.joinpath(ef.ap.name.replace('.ap.', '.sync.')).with_suffix('.npy')
        if not sync_file.exists():
            error_msg = f'No synchronisation file for {sync_file}'
            _logger.error(error_msg)
            raise FileNotFoundError(error_msg)
        sync_points = np.load(sync_file)
        fcn = interp1d(sync_points[:, 0],
                       sync_points[:, 1], fill_value='extrapolate')
        # patch the spikes.times files manually
        st_file = ses_path.joinpath(probe_out_path, 'spikes.times.npy')
        interp_times = fcn(np.load(st_file))
        np.save(st_file, interp_times)


def ks2_to_alf(ks_path, out_path, label=None, force=True):
    """
    Convert Kilosort 2 output to ALF dataset for single probe data
    :param ks_path:
    :param out_path:
    :return:
    """
    m = ephysqc.phy_model_from_ks2_path(ks_path)
    ac = alf.EphysAlfCreator(m)
    ac.convert(out_path, label=label, force=force)

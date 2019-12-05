#!/usr/bin/python
# Electrode fall off detection added
# Missing channel detection added, Now some channels can be missing
# Updated to support the new NEO prediction system
# Z3Score will no longer support V1 CFS
# New version now includes EMG channel, CFS version is now 2
# additional vectorization applied for higher speeds
# If the data is completely unprocessed, it has very large voltage low frequency noise
# this can mess up the processing, a DC blocking filter is applied to EEG and ECG channels 
# to mitigate the issue
# modified to be compatible with python 3
# function to read, write and create CFS stream (byte array) from raw PSG data
# (c)-2019 Neurobit Technologies Pte Ltd - Amiya Patanaik amiya@neurobit.io
#
# Licensed under GPL v3 for alternative license contact sales@neurobit.io
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math
import base64
import hashlib
import struct
import zlib
import msgpack
import warnings
import numpy as np
from io import BytesIO
import bottleneck as bn
from msgpack import unpackb
from scipy.interpolate import interp1d
from skimage.measure import block_reduce
from scipy.signal import firwin, lfilter, resample_poly, stft

def dc_block(x, fs, fc = 0.1):
# DC block filter the time signal x(t), fs is the sampling rate and 
# fc is the highpass cutoff frequency 
    Fc = 2.0*fc/fs
    a = (np.sqrt(3) - 2.0*math.sin(math.pi*Fc))/(math.sin(math.pi*Fc)+np.sqrt(3)*math.cos(math.pi*Fc))
    return lfilter([1, -1], [1, -a], x)
    

def create_stream_v3(data, sampling_rates, compressionbit=True, hashbit=True, check_quality = True):
# Order of data(12 channels cell array of 1Xsamples PSG data): 
# C3, C4, EOG-l, EOG-R, EMG-chin, EMG-left, 
# EMG-right, ECG, Airflow, Thor, Abdo, SpO2 and Corresponding sampling rates as a numpy array
# a new dc-block filter is added now to EEG and ECG channels, other channels are not touched

    data_exists = np.zeros(12)
    for idx, value in enumerate(data):
        if np.any(value):
            data_exists[idx] = 1  

    idx = np.where(data_exists == 1)
    idx = idx[0]

    if data_exists[0] == 0:
        sampling_rates[0] = sampling_rates[1]

    if data_exists[1] == 0:
        sampling_rates[1] = sampling_rates[0]

    if sampling_rates[1] != sampling_rates[0]:
        raise RuntimeError("Both EEG channels must be sampled at the same rate.")

    # check sampling rates
    if np.any(sampling_rates[0:2] < 100):
        raise RuntimeError("Sampling rate must be >= 100Hz for EEG channels.")

    if np.any(sampling_rates[2:4] < 100):
        raise RuntimeError("Sampling rate must be >= 100Hz for EOG channels.")

    if np.any(sampling_rates[4:7] < 200):
        raise RuntimeError("Sampling rate must be >= 200Hz for EMG channels.")

    if sampling_rates[7] < 200:
        raise RuntimeError("Sampling rate must be >= 200Hz for ECG channels.")

    if np.any(sampling_rates[8:11] < 25):
        raise RuntimeError("Sampling rate must be >= 25Hz for respiratory channels")

    if np.any(sampling_rates[11] < 1):
        raise RuntimeError("Sampling rate must be >= 1Hz for SpO2 channel")

    # Order 50 FIR filter
    # Basic Settings C3, C4, EOG-l, EOG-R, EMG-chin, EMG-left, 
    # EMG-right, ECG, Airflow, Thor, Abdo
    filter_lp = [35, 35, 35, 35, 80, 80, 80, 80, 15, 15, 15]
    filter_hp = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.05, 0.05, 0.05]
    filter_b = [None]*12
    processed_data = [[None]]*12
    one = np.array(1)

    for i in idx:
        if i == 11:
            # SpO2 channel 
            # resample to 1 Hz using nearest neighbour
            f = interp1d(np.arange(data[i].size), data[i], kind='nearest')
            processed_data[i] = f(np.arange(0, data[i].size, int(sampling_rates[i])))
            continue

        # check if EEG/EOG/ECG channel
        # apply a sharp DC block at 0.1 Hz
        if i < 8:
            data[i] = dc_block(data[i], sampling_rates[i])
        
        filter_b[i] = firwin(51, [filter_hp[i]*2 / sampling_rates[i], filter_lp[i]*2 / sampling_rates[i]], pass_zero=False, window='hamming', scale=True)
        processed_data[i] = lfilter(filter_b[i], one, data[i])
        

    threshold = 10

    # Process EEG
    eeg_exist = 0
    if data_exists[0] and data_exists[1]:
        eeg = (processed_data[0] + processed_data[1])/2
        eeg_exist = 1
    elif data_exists[0]:
        eeg = processed_data[0]
        eeg_exist = 1
    elif data_exists[1]:
        eeg = processed_data[1]
        eeg_exist = 1

    if eeg_exist:
        if sampling_rates[0] != 100:
            P = 100
            Q = sampling_rates[0]
            eeg = resample_poly(eeg, P, Q)
            processed_data[0] = eeg
            processed_data[1] = eeg

    # Process EOG
    for i in range(2,4):
        if data_exists[i] and sampling_rates[i] != 100:
            P = 100
            Q = sampling_rates[i]
            processed_data[i] = resample_poly(processed_data[i], P, Q)

    # Process EMG & ECG
    for i in range(4,8):
        if data_exists[i] and sampling_rates[i] != 200:
            P = 200
            Q = sampling_rates[i]
            processed_data[i] = resample_poly(processed_data[i], P, Q)
            if i == 7:
                aux = {'ECG': processed_data[i].tolist()}

    # Process Respiration
    for i in range(8,11):
        if data_exists[i] and sampling_rates[i] != 25:
            P = 25
            Q = sampling_rates[i]
            processed_data[i] = resample_poly(processed_data[i], P, Q)

    # release memory
    data = []

    rates = [100, 100, 100, 100, 200, 200, 200, 200, 25, 25, 25]
    totalEpochs = math.floor(processed_data[idx[0]].size/30/rates[idx[0]])

    data = np.zeros((32,32,10,totalEpochs), dtype=np.float32)
    window_128 = np.hamming(128)
    window_256 = np.hamming(256)

    for i in range(totalEpochs):
        if eeg_exist:
            frame = stft(eeg[i * 3000:(i + 1) * 3000], window=window_128, noverlap=36, boundary=None, nperseg=128,
                      return_onesided=True, padded=False)
            data[:, :, 0, i] = abs(frame[2][1:33, 0:32]) * np.sum(window_128)

        # EOG-L
        if data_exists[2]:
            frame = stft(processed_data[2][i * 3000:(i + 1) * 3000], window=window_128, noverlap=36, boundary=None, nperseg=128,
                      return_onesided=True, padded=False)
            data[:, :, 1, i] = abs(frame[2][1:33, 0:32]) * np.sum(window_128)

        # EOG-R
        if data_exists[3]:
            frame = stft(processed_data[3][i * 3000:(i + 1) * 3000], window=window_128, noverlap=36, boundary=None, nperseg=128,
                      return_onesided=True, padded=False)
            data[:, :, 2, i] = abs(frame[2][1:33, 0:32]) * np.sum(window_128)

        # EMG chin
        if data_exists[4]:
            frame = stft(processed_data[4][i * 6000:(i + 1) * 6000], window=window_256, noverlap=71, boundary=None, nperseg=256,
                      return_onesided=True, padded=False) 
            data[:, :, 3, i] = block_reduce(abs(frame[2][1:129, :]) * np.sum(window_256), (4, 1), np.mean) 

        # EMG leg left
        if data_exists[5]:
            frame = stft(processed_data[5][i * 6000:(i + 1) * 6000], window=window_256, noverlap=71, boundary=None, nperseg=256,
                      return_onesided=True, padded=False) 
            data[:, :, 4, i] = block_reduce(abs(frame[2][1:129, :]) * np.sum(window_256), (4, 1), np.mean) 

        # EMG leg right
        if data_exists[6]:
            frame = stft(processed_data[6][i * 6000:(i + 1) * 6000], window=window_256, noverlap=71, boundary=None, nperseg=256,
                      return_onesided=True, padded=False) 
            data[:, :, 5, i] = block_reduce(abs(frame[2][1:129, :]) * np.sum(window_256), (4, 1), np.mean)


    # ECG - no windowing 
    if data_exists[7]:
        frame = stft(processed_data[7], fs=200 ,window=window_256, noverlap=69, boundary=None, nperseg=256,
                      return_onesided=True, padded=True) 
        t = frame[1]-34.0/200.0
        frame = block_reduce(abs(frame[2][1:129, :]) * np.sum(window_256), (4, 1), np.mean)
        t0 =  np.linspace(0, totalEpochs*30, num=totalEpochs+1)
        idx = []
        for t_ in t0:
            idx.append(np.searchsorted(t, t_, side="right"))

        for j in range(totalEpochs):
            n = idx[j]
            if n+32 - np.shape(frame)[1] > 0:
                n = np.shape(frame)[1] - 32

            data[:, :, 6, j] = frame[:,n:n+32]

        
    # Respiration 
    for i in range(8, 11):
        if data_exists[i]:
            # data normalization
            mu = bn.move_mean(processed_data[i], window=25*60*18, min_count=1)
            sigma = bn.move_std(processed_data[i], window=25*60*18, min_count=1)
            sigma = sigma + (sigma == 0)*np.finfo(np.float).eps
            processed_data[i] = (processed_data[i] - mu)/sigma
            # stft
            frame = stft(processed_data[i], fs=25 ,window=window_256, noverlap=233, boundary=None, nperseg=256,
                      return_onesided=True, padded=True)
            t = frame[1] - 116/25
            t0 =  np.linspace(0, totalEpochs*30, num=totalEpochs+1)
            idx = []
            for t_ in t0:
                idx.append(np.searchsorted(t, t_, side="right"))

            for j in range(totalEpochs):
                n = idx[j]
                if n+32 - np.shape(frame[2])[1] > 0:
                    n = np.shape(frame[2])[1] - 32

                data[:, :, i-1, j] = abs(frame[2][1:33,n:n+32])

    # SpO2 sampled at 1 Hz 
    spo2 = np.zeros(totalEpochs*30, dtype=np.float32)
    if data_exists[11]:
        spo2[:] = processed_data[11][0:totalEpochs*30]
        ceiling = np.quantile(spo2,0.999)/100
        spo2 = 100 - spo2/ceiling
        spo2[spo2 > 50] = 50
        spo2[spo2 < 0] = 0

        

    
    quality = np.sum(np.mean(data, axis=(0,1)) > 500, axis = 1)*100.0/totalEpochs

    if np.any(quality > threshold) and check_quality:
        print("\u001b[31;1mWARNING:\u001b[0m Electrode Falloff detected, problematic channels will be ignored.")

    if np.sum(data_exists[0:5]) == 0:
        print("\u001b[31;1mWARNING:\u001b[0m No EEG channel found, sleep staging cannot be done.")
    
    #if np.sum(data_exists[5:7]) == 0:
    #    print("\u001b[31;1mWARNING:\u001b[0m Leg EMG not found, PLM detection disabled.")

    #if np.sum(data_exists[8:11]) == 0:
    #    print("\u001b[31;1mWARNING:\u001b[0m No respiratory channel found, respiratory events detection disabled.")
    
    signature = bytearray(
        struct.pack('<3sBBBBh??', b'CFS', 3, 32, 32, 10, totalEpochs, compressionbit, hashbit))
  
    data = data.flatten('F')
    data = data.tostring()

    if data_exists[7]:
        data = data + spo2.tostring() + msgpack.packb(aux)
    else:
        data = data + spo2.tostring()

    raw_digest = []
    if hashbit:
        shaHash = hashlib.sha1()
        shaHash.update(data)
        raw_digest = shaHash.digest()

    if compressionbit:
        data = zlib.compress(data)

    if hashbit:
        stream = signature + raw_digest + data 
    else:
        stream = signature + data

    return stream


def create_stream_v2(C3, C4, EOGL, EOGR, EMG, sampling_rates, compressionbit=True, hashbit=True, check_quality = True):
    SRATE = 100  # Hz
    LOWPASS = 35.0  # Hz
    HIGHPASS = 0.3  # Hz
    LOWPASSEOG = 35.0  # Hz
    LOWPASSEMG = 80.0  # Hz
    channels = 5  # 2EEG 2EOG 1EMG

    if (sampling_rates[0] < 100 or sampling_rates[1] < 100 or sampling_rates[2] < 200):
        raise RuntimeError("Sampling rate too low.")

    # Apply DC block 
    C3 = dc_block(C3, sampling_rates[0])
    C4 = dc_block(C4, sampling_rates[0])
    EOGL = dc_block(EOGL, sampling_rates[1])
    EOGR = dc_block(EOGR, sampling_rates[1])
    EMG = dc_block(EMG, sampling_rates[2])

    Fs_EEG = sampling_rates[0] / 2.0
    Fs_EOG = sampling_rates[1] / 2.0
    Fs_EMG = sampling_rates[2] / 2.0

    one = np.array(1)

    bEEG = firwin(51, [HIGHPASS / Fs_EEG, LOWPASS / Fs_EEG], pass_zero=False, window='hamming', scale=True)
    bEOG = firwin(51, [HIGHPASS / Fs_EOG, LOWPASSEOG / Fs_EOG], pass_zero=False, window='hamming', scale=True)
    bEMG = firwin(51, [HIGHPASS / Fs_EMG, LOWPASSEMG / Fs_EMG], pass_zero=False, window='hamming', scale=True)

    eogL = lfilter(bEOG, one, EOGL)
    eogR = lfilter(bEOG, one, EOGR)
    eeg = (lfilter(bEEG, one, C3) + lfilter(bEEG, one, C4)) / 2.0
    emg = lfilter(bEMG, one, EMG)

    if sampling_rates[0] != 100:
        P = 100
        Q = sampling_rates[0]
        eeg = resample_poly(eeg, P, Q)

    if sampling_rates[1] != 100:
        P = 100
        Q = sampling_rates[1]
        eogL = resample_poly(eogL, P, Q)
        eogR = resample_poly(eogR, P, Q)

    if sampling_rates[2] != 200:
        P = 200
        Q = sampling_rates[2]
        emg = resample_poly(emg, P, Q)

    totalEpochs = int(len(eogL) / 30.0 / SRATE)
    data_length = 32 * 32 * (channels - 1) * totalEpochs
    data = np.empty([data_length], dtype=np.float32)
    window_eog = np.hamming(128)
    window_eeg = np.hamming(128)
    window_emg = np.hamming(256)
    epochSize = 32 * 32 * (channels - 1)
    data_frame = np.empty([32, 32, channels - 1])
    mean_power = np.empty([channels - 1, totalEpochs])

    # spectrogram computation
    for i in range(totalEpochs):
        frame1 = stft(eeg[i * 3000:(i + 1) * 3000], window=window_eeg, noverlap=36, boundary=None, nperseg=128,
                      return_onesided=True, padded=False)
        frame2 = stft(eogL[i * 3000:(i + 1) * 3000], window=window_eog, noverlap=36, boundary=None, nperseg=128,
                      return_onesided=True, padded=False)
        frame3 = stft(eogR[i * 3000:(i + 1) * 3000], window=window_eog, noverlap=36, boundary=None, nperseg=128,
                      return_onesided=True, padded=False)
        frame4 = stft(emg[i * 6000:(i + 1) * 6000], window=window_emg, noverlap=71, boundary=None, nperseg=256,
                      return_onesided=True, padded=False)

        data_frame[:, :, 0] = abs(frame1[2][1:33, 0:32]) * np.sum(window_eeg)  # EEG
        data_frame[:, :, 1] = abs(frame2[2][1:33, 0:32]) * np.sum(window_eog)  # EOG-L
        data_frame[:, :, 2] = abs(frame3[2][1:33, 0:32]) * np.sum(window_eog)  # EOG-R
        data_frame[:, :, 3] = block_reduce(abs(frame4[2][1:129, :]) * np.sum(window_emg), (4, 1), np.mean)   # EMG
        mean_power[:, i] = np.mean(data_frame, (0, 1))

        data[i * epochSize:(i + 1) * epochSize] = np.reshape(data_frame, epochSize, order='F')

    
    quality = np.sum(mean_power > 800,1)*100/totalEpochs

    if np.any(quality > 10) and check_quality:
        print("Warning: Electrode Falloff detected, use qc_cfs function to check which channel is problematic")
        
    signature = bytearray(
        struct.pack('<3sBBBBh??', b'CFS', 2, 32, 32, (channels - 1), totalEpochs, compressionbit, hashbit))

    data = data.tostring()

    raw_digest = []
    if hashbit:
        shaHash = hashlib.sha1()
        shaHash.update(data)
        raw_digest = shaHash.digest()

    if compressionbit:
        data = zlib.compress(data)

    if hashbit:
        stream = signature + raw_digest + data
    else:
        stream = signature + data

    return stream


def save_stream_v2(file_name, C3, C4, EOGL, EOGR, EMG, sampling_rates, compressionbit=True, hashbit=True, check_quality=True):
    stream = create_stream_v2(C3, C4, EOGL, EOGR, EMG, sampling_rates, compressionbit=compressionbit, hashbit=hashbit, check_quality=check_quality)

    with open(file_name, 'wb') as f:
        f.write(stream)

    return stream



def create_stream(EEG_data, sampling_rate, compressionbit=True, hashbit=True, check_quality=True):
    warnings.warn('You are using version 1 of CFS, CFS version 1 is deprecated and will not be supported by Z3Score in the future.', RuntimeWarning)
    
    # apply DC block filter 
    for i in range(4):
        EEG_data[i,:] = dc_block(EEG_data[i,:], sampling_rate)

    SRATE = 100 #Hz
    LOWPASS = 45.0 #Hz
    HIGHPASS = 0.3 #Hz
    LOWPASSEOG = 12.0 #Hz
    Fs = sampling_rate/2.0
    one = np.array(1)
    bEEG = firwin(51, [HIGHPASS / Fs, LOWPASS / Fs], pass_zero=False, window='hamming', scale=True)
    bEOG = firwin(51, [HIGHPASS / Fs, LOWPASSEOG / Fs], pass_zero=False, window='hamming', scale=True)
    eogL = lfilter(bEOG,one,EEG_data[2,:])
    eogR = lfilter(bEOG,one,EEG_data[3,:])
    eeg = (lfilter(bEEG,one,EEG_data[0,:]) + lfilter(bEEG,one,EEG_data[1,:]))/2.0

    if sampling_rate != 100:
        P = 100
        Q = sampling_rate
        eogL = resample_poly(eogL,P,Q)
        eogR = resample_poly(eogR,P,Q)
        eeg = resample_poly(eeg,P,Q)

    totalEpochs = int(len(eogL)/30.0/SRATE)
    data_length = 32*32*3*totalEpochs
    mean_power = np.empty((3, totalEpochs))
    data = np.empty([data_length], dtype=np.float32)
    window = np.hamming(128)
    epochSize = 32 * 32 * 3

    #STFT based spectrogram computation
    for i in range(totalEpochs):
        for j in range(0,3000-128-1,90):
            tIDX = int(j/90)
            frame1 = abs(np.fft.fft(eeg[i * 3000 + j: i * 3000 + j + 128]*window))
            frame2 = abs(np.fft.fft(eogL[i * 3000 + j: i * 3000 + j + 128] * window))
            frame3 = abs(np.fft.fft(eogR[i * 3000 + j: i * 3000 + j + 128] * window))
            mean_power[:, i] = [np.mean(frame1), np.mean(frame2), np.mean(frame3)]
            data[i*epochSize + tIDX * 32: i*epochSize + tIDX * 32 + 32] = frame1[0:32]
            data[i*epochSize + 32 * 32 + tIDX * 32: i*epochSize + 32 * 32 + tIDX * 32 + 32] = frame2[0:32]
            data[i*epochSize + 32 * 32 * 2 + tIDX * 32: i*epochSize + 32 * 32 * 2 + tIDX * 32 + 32] = frame3[0:32]


    quality = np.sum(mean_power > 800,1)*100/totalEpochs

    if np.any(quality > 10) and check_quality:
        print("Warning: Electrode Falloff detected, use qc_cfs function to check which channel is problematic")

    signature = bytearray(struct.pack('<3sBBBBh??', b'CFS',1,32,32,3,totalEpochs,compressionbit,hashbit))
    data = data.tostring()

    raw_digest = []
    if hashbit:
        shaHash = hashlib.sha1()
        shaHash.update(data)
        raw_digest = shaHash.digest()
    
    if compressionbit:
        data = zlib.compress(data)

    if hashbit:
        stream = signature + raw_digest + data
    else:
        stream = signature + data

    return stream


def save_stream(file_name, EEG_data, sampling_rate, compressionbit=True, hashbit=True, check_quality=True):

    stream = create_stream(EEG_data, sampling_rate, compressionbit, hashbit, check_quality)

    with open(file_name, 'wb') as f:
        f.write(stream)

    return stream


def read_stream_header(stream):
    # Read header:
    # 3 bytes signature, 1 byte version, 1 byte frequency, 1 byte time, 1 byte channel 2 bytes epochs
    # 1 byte compressionbit, 1 byte hashbit
    bytes = stream.read(11)
    header = struct.unpack('<3sBBBBh??', bytes)
    urlSafeHash = None
    digest = None

    if (header[0].decode("ascii") != 'CFS'):
        raise RuntimeError("File is not a valid CFS file.")

    if not (header[1] >= 1 and header[1] <= 3):
        raise RuntimeError("Invalid CFS version.")

    version = header[1]
    nfreq = header[2]
    ntime = header[3]
    nchannel = header[4]
    nepoch = header[5]
    compressionbit = header[6]
    hashbit = header[7]

    if (hashbit):
        # read SHA hash
        bytes = stream.read(20)
        digest = struct.unpack('<20B', bytes)
        urlSafeHash = base64.urlsafe_b64encode(("".join(map(chr, digest))).encode('UTF-8')).decode('ascii')
        urlSafeHash = urlSafeHash[0:-1]
    
    stream.seek(0)

    header = {'freq': nfreq, 'time': ntime, 'channel': nchannel, 'version': version,
              'epoch': nepoch, 'compression': compressionbit, 'hash': hashbit, 'url': urlSafeHash}
    
    return header



def read_stream(stream, check_quality = True):
    # Read header:
    # 3 bytes signature, 1 byte version, 1 byte frequency, 1 byte time, 1 byte channel 2 bytes epochs
    # 1 byte compressionbit, 1 byte hashbit
    bytes = stream.read(11)
    header = struct.unpack('<3sBBBBh??', bytes)
    urlSafeHash = None
    digest = None

    if (header[0].decode("ascii") != 'CFS'):
        raise RuntimeError("File is not a valid CFS file.")

    if not (header[1] >= 1 and header[1] <= 3):
        raise RuntimeError("Invalid CFS version.")

    version = header[1]
    nfreq = header[2]
    ntime = header[3]
    nchannel = header[4]
    nepoch = header[5]
    compressionbit = header[6]
    hashbit = header[7]

    if (hashbit):
        # read SHA hash
        bytes = stream.read(20)
        digest = struct.unpack('<20B', bytes)
        urlSafeHash = base64.urlsafe_b64encode(("".join(map(chr, digest))).encode('UTF-8')).decode('ascii')
        urlSafeHash = urlSafeHash[0:-1]

    # read rest of the data
    bytes = stream.read()

    if (compressionbit):
        bytes = zlib.decompress(bytes)

    base_size = struct.calcsize('<' + str(nfreq * ntime * nchannel * nepoch) + 'f')
    rawStream = struct.unpack('<' + str(nfreq * ntime * nchannel * nepoch) + 'f', bytes[0:base_size])

    if version == 3:
        spo2_size = struct.calcsize('<1f')* 30 * nepoch
        rr_size = len(bytes) - base_size - spo2_size

        spo2 = struct.unpack('<' + str(30 * nepoch) + 'f', bytes[base_size:base_size + struct.calcsize('<1f')* 30 * nepoch])

        if rr_size > 0:
            rr =  unpackb(bytes[base_size + spo2_size:])
        else:
            rr = None


    if (hashbit):
        shaHash = hashlib.sha1()
        shaHash.update(bytes)
        rawDigest = shaHash.digest()
        msgDigest = [c for c in rawDigest]

        if (tuple(msgDigest) != digest):
            raise RuntimeError("File is corrupt.")

    dataStream = np.asarray(rawStream, dtype='float32')
    dataStream = np.reshape(dataStream, (nfreq, ntime, nchannel, nepoch), order="F")

    quality = np.sum(np.mean(dataStream,(0,1)) > 800,1)*100/np.shape(dataStream)[-1]
    if np.any(quality > 10) and check_quality:
        print("Warning: Electrode Falloff detected, use qc_cfs function to check which channel is problematic")

    channels_absent = np.std(dataStream, (0,1,3)) < 1
    if np.any(channels_absent) and check_quality:
        print("Warning: Some channels are missing, ignore if this is intentional otherwise use qc_cfs function")

    stream.seek(0)

    header = {'freq': nfreq, 'time': ntime, 'channel': nchannel, 'version': version,
              'epoch': nepoch, 'compression': compressionbit, 'hash': hashbit, 'url': urlSafeHash}

    if version == 3:
        return dataStream, header, spo2, rr
    else:
        return dataStream, header


def read_header(cfs_file):
    # Read header:
    # 3 bytes signature, 1 byte version, 1 byte frequency, 1 byte time, 1 byte channel 2 bytes epochs
    # 1 byte compressionbit, 1 byte hashbit
    stream = open(cfs_file, "rb")
    bytes = stream.read(11)
    header = struct.unpack('<3sBBBBh??', bytes)

    if (header[0].decode("ascii") != 'CFS'):
        raise RuntimeError("File is not a valid CFS file.")

    if (header[1] < 1 or header[1] > 3):
        raise RuntimeError("Invalid CFS version.")

    version = header[1]
    nfreq = header[2]
    ntime = header[3]
    nchannel = header[4]
    nepoch = header[5]
    compressionbit = header[6]
    hashbit = header[7]

    urlSafeHash = None

    if (hashbit):
        # read SHA hash
        bytes = stream.read(20)
        digest = struct.unpack('<20B', bytes)
        urlSafeHash = base64.urlsafe_b64encode(("".join(map(chr, digest))).encode('UTF-8')).decode('ascii')
        urlSafeHash = urlSafeHash[0:-1]

    stream.seek(0)

    header = {'freq': nfreq, 'time': ntime, 'channel': nchannel, 'version': version,
              'epoch': nepoch, 'compression': compressionbit, 'hash': hashbit, 'url': urlSafeHash}
    return header


def read_cfs(cfs_file, check_quality = True):
    stream = open(cfs_file, "rb")
    return read_stream(stream, check_quality)


def qc_cfs(cfs_file, threshold = 10):
    data, header = read_cfs(cfs_file, check_quality = False)
    quality = np.sum(np.mean(data,(0,1)) > 800,1)*100/np.shape(data)[-1]
    channels_absent = np.std(data, (0,1,3)) < 1
    electrodes = {
        0: "C3/C4",
        1: "EOG-left",
        2: "EOG-right",
        3: "EMG-Chin",
        4: "EMG-Leg-Left",
        5: "EMG-Leg-Right",
        6: "ECG",
        7: "Airflow",
        8: "Thor",
        9: "Abdo",
    }
    status = False
    qc = quality > threshold
    idx = np.flatnonzero(qc)
    failed_channels = " "
    message = "All channels passed quality checks."
    
    if np.any(qc):
        status = True
        for i in idx:
            failed_channels += electrodes[i] + ", "
        message = "The following channel(s) failed quality checks: " + failed_channels 

    idx = np.flatnonzero(channels_absent)
    message_missing = ""
    if np.any(channels_absent):
        for i in idx:
            failed_channels += electrodes[i] + ", "
            quality[i] = -1
        if status:
            message_missing = "\nThe following channel(s) are missing: " + failed_channels
        else:
            message_missing = "The following channel(s) are missing: " + failed_channels 


    return status, quality, message + message_missing


def qc_stream(bytestream, threshold = 10):
    file_stream = BytesIO(bytestream)
    data, header = read_stream(file_stream, check_quality = False)
    quality = np.sum(np.mean(data,(0,1)) > 800,1)*100/np.shape(data)[-1]
    channels_absent = np.std(data, (0,1,3)) < 1
    electrodes = {
        0: "C3/C4",
        1: "EOG-left",
        2: "EOG-right",
        3: "EMG-Chin",
        4: "EMG-Leg-Left",
        5: "EMG-Leg-Right",
        6: "ECG",
        7: "Airflow",
        8: "Thor",
        9: "Abdo",
    }
    status = False
    qc = quality > threshold
    idx = np.flatnonzero(qc)
    failed_channels = " "
    message = "All channels passed quality checks."

    if np.any(qc):
        status = True
        for i in idx:
            failed_channels += electrodes[i] + ", "
        message = "The following channel(s) failed quality checks: " + failed_channels

    idx = np.flatnonzero(channels_absent)
    message_missing = ""
    if np.any(channels_absent):
        for i in idx:
            failed_channels += electrodes[i] + ", "
            quality[i] = -1
        if status:
            message_missing = "\nThe following channel(s) are missing: " + failed_channels
        else:
            message_missing = "The following channel(s) are missing: " + failed_channels 

    return status, quality, message + message_missing


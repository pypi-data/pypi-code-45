import sys
sys.path.append("src/util")

from audacity_pipe import do_command
from glob import glob
from instruments import instruments
from __init__ import predict
import os
import soundfile as sf

AUDACITY_DIR = "data/audacity"

def get_active_wav():
    wav_regexp = f"{AUDACITY_DIR}/macro-output/*.wav"
    old_files = set(glob(wav_regexp))
    do_command('ExportWav:')
    new_files = set(glob(wav_regexp))
    return list(old_files ^ new_files)[0]

if __name__ == "__main__":
    filename = get_active_wav()
    sig, fs = sf.read(filename)
    os.remove(filename)
    timestamps = predict(sig, sample_rate=fs)
    
    label_file = open(f"{AUDACITY_DIR}/labels.txt","w+")
    for i, timestamp in enumerate(timestamps):
        if timestamp:
            for time_range in timestamp:
                label_file.write(f"{time_range[0]}\t{time_range[1]}\t{instruments[i]}\n")
    label_file.close()
    do_command('ImportLabels:')

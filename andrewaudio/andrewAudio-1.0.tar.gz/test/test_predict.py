import sys
sys.path.append("src")
sys.path.append("src/util")
sys.path.append("data/audio/test")

import numpy as np
import os
import soundfile as sf
from __init__ import extract_features, get_n_way, get_timestamps
from instruments import instruments

TEST_PATH = "data/audio/test"

if __name__ == '__main__':
    for filename in os.listdir(TEST_PATH):
        if filename.endswith(".wav"):
            print(f"{filename}:")
            sig, fs = sf.read(f"{TEST_PATH}/{filename}")
            data_loader = extract_features(sig, fs)
            data = get_n_way(data_loader)

            for n in range(16):
                timestamps = get_timestamps(data, n)
                if len(timestamps) > 0:
                    print(f"{instruments[n]}: {timestamps}")
            print("")

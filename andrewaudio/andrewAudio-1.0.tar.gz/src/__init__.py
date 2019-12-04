import sys
sys.path.append("src/feature_extract")
sys.path.append("src/model")

import math
import pandas as pd
import torch

from feature_extract import extract
from train import parse_audio_data, train_audio_set
from run import run

def extract_features(data, sample_rate):
    """Extract audio features from input data

    Args:
        data: MxN numpy.array, where M is number of samples and N is channels
        sample_rate

    Returns:
        pytorch.DataLoader
    """

    # Get features of each segment
    # Each row of output corresponds to 0.96s of audio - shape should be (NUM_SECONDS, 128)
    features = extract(data, sample_rate)

    # Get features data into pandas dataframe
    data = pd.DataFrame(features)
    data_loader, _ = parse_audio_data(data, train_test_ratio=1.0)

    return data_loader

def get_n_way(test_loader, FILE_NAME="FreeSound"):
    """Generate a probability distribution of each label in intervals given an input audio track

    Args:
        test_loader: pytorch.DataLoader - contains audio feature data

    Returns:
        2D numpy array - probability of each class in each second
    """

    # Load network weights and architecture
    dnn = torch.load(f'data/models/{FILE_NAME}_model.pt')

    # Find n-way class prediction distribution of each sample
    data = run(dnn, test_loader)

    return data

def get_timestamps(data, label, threshold=0.1):
    """Wrapper function for model usage
    
    Args:
        data: MxN numpy.array, where M is number of samples and N is channels
        label: int, Index of the label to predict in range [0, NUM_CLASSES)
        sample_rate

    Returns:
        2D numpy array (Mx2, where M is number of regions) containing start and end timestamps (in ms) for predicted region
    """

    threshold = math.log(threshold, 10)

    # Merge algorithm between consecutive segments with probability of given label above threshold
    timestamps = []
    if label is None:
        NUM_CLASSES = 16
        for n in range(NUM_CLASSES):
            i = 0
            ith_timestamps = []
            while i < len(data):
                if data[i][n] > threshold:
                    start = i
                    while i < len(data) and data[i][n] > threshold:
                        i += 1
                    ith_timestamps.append((start, i - 1))
                i += 1
            timestamps.append(ith_timestamps)
    else:
        i = 0
        while i < len(data):
            if data[i][label] > threshold:
                start = i
                while i < len(data) and data[i][label] > threshold:
                    i += 1
                timestamps.append((start, i - 1))
            i += 1

    return timestamps

def predict(data, label=None, sample_rate=44100):
    """Wrapper function for model usage
    
    Args:
        data: MxN numpy.array, where M is number of samples and N is channels
        label: string, The label to predict
        sample_rate

    Returns:
        2D numpy array containing start and end timestamps (in ms) for predicted region
    """

    # Get audio features
    test_loader = extract_features(data, sample_rate)

    # Get an array of probability distributions from network
    n_way_data = get_n_way(test_loader)

    # Return predicted high-probability regions
    timestamps = get_timestamps(n_way_data, label)

    return timestamps

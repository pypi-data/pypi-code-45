from enum import Enum


class DataSourceLabel(Enum):
    PREDICTION = 'predict'
    TEST = 'test'
    TRAIN = 'train'

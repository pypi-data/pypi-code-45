# coding: utf-8

"""
    BlackFox

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from blackfox_restapi.models.keras_hidden_layer_config import KerasHiddenLayerConfig  # noqa: F401,E501
from blackfox_restapi.models.keras_layer_config import KerasLayerConfig  # noqa: F401,E501
from blackfox_restapi.models.range import Range  # noqa: F401,E501


class KerasTrainingConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'batch_size': 'int',
        'dataset_id': 'str',
        'input_ranges': 'list[Range]',
        'output_layer': 'KerasLayerConfig',
        'hidden_layer_configs': 'list[KerasHiddenLayerConfig]',
        'training_algorithm': 'str',
        'max_epoch': 'int',
        'cross_validation': 'bool',
        'validation_split': 'float',
        'random_seed': 'int'
    }

    attribute_map = {
        'batch_size': 'batchSize',
        'dataset_id': 'datasetId',
        'input_ranges': 'inputRanges',
        'output_layer': 'outputLayer',
        'hidden_layer_configs': 'hiddenLayerConfigs',
        'training_algorithm': 'trainingAlgorithm',
        'max_epoch': 'maxEpoch',
        'cross_validation': 'crossValidation',
        'validation_split': 'validationSplit',
        'random_seed': 'randomSeed'
    }

    def __init__(self, batch_size=None, dataset_id=None, input_ranges=None, output_layer=None, hidden_layer_configs=None, training_algorithm=None, max_epoch=None, cross_validation=None, validation_split=None, random_seed=None):  # noqa: E501
        """KerasTrainingConfig - a model defined in Swagger"""  # noqa: E501

        self._batch_size = None
        self._dataset_id = None
        self._input_ranges = None
        self._output_layer = None
        self._hidden_layer_configs = None
        self._training_algorithm = None
        self._max_epoch = None
        self._cross_validation = None
        self._validation_split = None
        self._random_seed = None
        self.discriminator = None

        if batch_size is not None:
            self.batch_size = batch_size
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if input_ranges is not None:
            self.input_ranges = input_ranges
        if output_layer is not None:
            self.output_layer = output_layer
        if hidden_layer_configs is not None:
            self.hidden_layer_configs = hidden_layer_configs
        if training_algorithm is not None:
            self.training_algorithm = training_algorithm
        self.max_epoch = max_epoch
        if cross_validation is not None:
            self.cross_validation = cross_validation
        self.validation_split = validation_split
        if random_seed is not None:
            self.random_seed = random_seed

    @property
    def batch_size(self):
        """Gets the batch_size of this KerasTrainingConfig.  # noqa: E501

        Training batch size  # noqa: E501

        :return: The batch_size of this KerasTrainingConfig.  # noqa: E501
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this KerasTrainingConfig.

        Training batch size  # noqa: E501

        :param batch_size: The batch_size of this KerasTrainingConfig.  # noqa: E501
        :type: int
        """

        self._batch_size = batch_size

    @property
    def dataset_id(self):
        """Gets the dataset_id of this KerasTrainingConfig.  # noqa: E501

        Data set id on which to train network  # noqa: E501

        :return: The dataset_id of this KerasTrainingConfig.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this KerasTrainingConfig.

        Data set id on which to train network  # noqa: E501

        :param dataset_id: The dataset_id of this KerasTrainingConfig.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def input_ranges(self):
        """Gets the input_ranges of this KerasTrainingConfig.  # noqa: E501

        Define min and max value for each input column(feature)  # noqa: E501

        :return: The input_ranges of this KerasTrainingConfig.  # noqa: E501
        :rtype: list[Range]
        """
        return self._input_ranges

    @input_ranges.setter
    def input_ranges(self, input_ranges):
        """Sets the input_ranges of this KerasTrainingConfig.

        Define min and max value for each input column(feature)  # noqa: E501

        :param input_ranges: The input_ranges of this KerasTrainingConfig.  # noqa: E501
        :type: list[Range]
        """

        self._input_ranges = input_ranges

    @property
    def output_layer(self):
        """Gets the output_layer of this KerasTrainingConfig.  # noqa: E501

        Define min and max value for each output column(feature), and output activation function  # noqa: E501

        :return: The output_layer of this KerasTrainingConfig.  # noqa: E501
        :rtype: KerasLayerConfig
        """
        return self._output_layer

    @output_layer.setter
    def output_layer(self, output_layer):
        """Sets the output_layer of this KerasTrainingConfig.

        Define min and max value for each output column(feature), and output activation function  # noqa: E501

        :param output_layer: The output_layer of this KerasTrainingConfig.  # noqa: E501
        :type: KerasLayerConfig
        """

        self._output_layer = output_layer

    @property
    def hidden_layer_configs(self):
        """Gets the hidden_layer_configs of this KerasTrainingConfig.  # noqa: E501

        Hidden layers configuration  # noqa: E501

        :return: The hidden_layer_configs of this KerasTrainingConfig.  # noqa: E501
        :rtype: list[KerasHiddenLayerConfig]
        """
        return self._hidden_layer_configs

    @hidden_layer_configs.setter
    def hidden_layer_configs(self, hidden_layer_configs):
        """Sets the hidden_layer_configs of this KerasTrainingConfig.

        Hidden layers configuration  # noqa: E501

        :param hidden_layer_configs: The hidden_layer_configs of this KerasTrainingConfig.  # noqa: E501
        :type: list[KerasHiddenLayerConfig]
        """

        self._hidden_layer_configs = hidden_layer_configs

    @property
    def training_algorithm(self):
        """Gets the training_algorithm of this KerasTrainingConfig.  # noqa: E501

        Training algorithm to use  # noqa: E501

        :return: The training_algorithm of this KerasTrainingConfig.  # noqa: E501
        :rtype: str
        """
        return self._training_algorithm

    @training_algorithm.setter
    def training_algorithm(self, training_algorithm):
        """Sets the training_algorithm of this KerasTrainingConfig.

        Training algorithm to use  # noqa: E501

        :param training_algorithm: The training_algorithm of this KerasTrainingConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["SGD", "RMSprop", "Adagrad", "Adadelta", "Adam", "Adamax", "Nadam"]  # noqa: E501
        if training_algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `training_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(training_algorithm, allowed_values)
            )

        self._training_algorithm = training_algorithm

    @property
    def max_epoch(self):
        """Gets the max_epoch of this KerasTrainingConfig.  # noqa: E501

        Maximum number of epoch  # noqa: E501

        :return: The max_epoch of this KerasTrainingConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_epoch

    @max_epoch.setter
    def max_epoch(self, max_epoch):
        """Sets the max_epoch of this KerasTrainingConfig.

        Maximum number of epoch  # noqa: E501

        :param max_epoch: The max_epoch of this KerasTrainingConfig.  # noqa: E501
        :type: int
        """
        if max_epoch is None:
            raise ValueError("Invalid value for `max_epoch`, must not be `None`")  # noqa: E501
        if max_epoch is not None and max_epoch > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `max_epoch`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if max_epoch is not None and max_epoch < 1:  # noqa: E501
            raise ValueError("Invalid value for `max_epoch`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_epoch = max_epoch

    @property
    def cross_validation(self):
        """Gets the cross_validation of this KerasTrainingConfig.  # noqa: E501

        Use cross validation  # noqa: E501

        :return: The cross_validation of this KerasTrainingConfig.  # noqa: E501
        :rtype: bool
        """
        return self._cross_validation

    @cross_validation.setter
    def cross_validation(self, cross_validation):
        """Sets the cross_validation of this KerasTrainingConfig.

        Use cross validation  # noqa: E501

        :param cross_validation: The cross_validation of this KerasTrainingConfig.  # noqa: E501
        :type: bool
        """

        self._cross_validation = cross_validation

    @property
    def validation_split(self):
        """Gets the validation_split of this KerasTrainingConfig.  # noqa: E501

        Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation = false.  # noqa: E501

        :return: The validation_split of this KerasTrainingConfig.  # noqa: E501
        :rtype: float
        """
        return self._validation_split

    @validation_split.setter
    def validation_split(self, validation_split):
        """Sets the validation_split of this KerasTrainingConfig.

        Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation = false.  # noqa: E501

        :param validation_split: The validation_split of this KerasTrainingConfig.  # noqa: E501
        :type: float
        """
        if validation_split is None:
            raise ValueError("Invalid value for `validation_split`, must not be `None`")  # noqa: E501
        if validation_split is not None and validation_split > 1.0:  # noqa: E501
            raise ValueError("Invalid value for `validation_split`, must be a value less than or equal to `1.0`")  # noqa: E501
        if validation_split is not None and validation_split < 0.0:  # noqa: E501
            raise ValueError("Invalid value for `validation_split`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._validation_split = validation_split

    @property
    def random_seed(self):
        """Gets the random_seed of this KerasTrainingConfig.  # noqa: E501

        Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation = false  # noqa: E501

        :return: The random_seed of this KerasTrainingConfig.  # noqa: E501
        :rtype: int
        """
        return self._random_seed

    @random_seed.setter
    def random_seed(self, random_seed):
        """Sets the random_seed of this KerasTrainingConfig.

        Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation = false  # noqa: E501

        :param random_seed: The random_seed of this KerasTrainingConfig.  # noqa: E501
        :type: int
        """

        self._random_seed = random_seed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(KerasTrainingConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KerasTrainingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

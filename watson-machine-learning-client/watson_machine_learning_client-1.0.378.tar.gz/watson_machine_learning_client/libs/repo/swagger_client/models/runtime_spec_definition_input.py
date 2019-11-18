# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class RuntimeSpecDefinitionInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, platform=None, custom_libraries=None, public_libraries=None ):
        """
        RuntimeSpecDefinitionInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'platform': 'RuntimeSpecDefinitionInputPlatform',
            'custom_libraries': 'RuntimeSpecDefinitionInputCustomLibraries',
            'public_libraries': 'list[RuntimeSpecDefinitionInputPublicLibraries]'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'platform': 'platform',
            'custom_libraries': 'custom_libraries',
            'public_libraries': 'public_libraries'
        }

        self._name = name
        self._description = description
        self._platform = platform
        self._custom_libraries = custom_libraries
        self._public_libraries = public_libraries

    @property
    def name(self):
        """
        Gets the name of this RuntimeSpecDefinitionInput.


        :return: The name of this RuntimeSpecDefinitionInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RuntimeSpecDefinitionInput.


        :param name: The name of this RuntimeSpecDefinitionInput.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this RuntimeSpecDefinitionInput.


        :return: The description of this RuntimeSpecDefinitionInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RuntimeSpecDefinitionInput.


        :param description: The description of this RuntimeSpecDefinitionInput.
        :type: str
        """
        self._description = description

    @property
    def platform(self):
        """
        Gets the platform of this RuntimeSpecDefinitionInput.


        :return: The platform of this RuntimeSpecDefinitionInput.
        :rtype: RuntimeSpecDefinitionInputPlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this RuntimeSpecDefinitionInput.


        :param platform: The platform of this RuntimeSpecDefinitionInput.
        :type: RuntimeSpecDefinitionInputPlatform
        """
        self._platform = platform

    @property
    def custom_libraries(self):
        """
        Gets the custom_libraries of this RuntimeSpecDefinitionInput.


        :return: The custom_libraries of this RuntimeSpecDefinitionInput.
        :rtype: RuntimeSpecDefinitionInputCustomLibraries
        """
        return self._custom_libraries

    @custom_libraries.setter
    def custom_libraries(self, custom_libraries):
        """
        Sets the custom_libraries of this RuntimeSpecDefinitionInput.


        :param custom_libraries: The custom_libraries of this RuntimeSpecDefinitionInput.
        :type: RuntimeSpecDefinitionInputCustomLibraries
        """
        self._custom_libraries = custom_libraries

    @property
    def public_libraries(self):
        """
        Gets the public_libraries of this RuntimeSpecDefinitionInput.
        Array of public libraries

        :return: The public_libraries of this RuntimeSpecDefinitionInput.
        :rtype: list[RuntimeSpecDefinitionInputPublicLibraries]
        """
        return self._public_libraries

    @public_libraries.setter
    def public_libraries(self, public_libraries):
        """
        Sets the public_libraries of this RuntimeSpecDefinitionInput.
        Array of public libraries

        :param public_libraries: The public_libraries of this RuntimeSpecDefinitionInput.
        :type: list[RuntimeSpecDefinitionInputPublicLibraries]
        """
        self._public_libraries = public_libraries

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other


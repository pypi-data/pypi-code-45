# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_rpm.configuration import Configuration


class RpmUpdateRecord(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'id': 'str',
        'updated_date': 'str',
        'description': 'str',
        'issued_date': 'str',
        'fromstr': 'str',
        'status': 'str',
        'title': 'str',
        'summary': 'str',
        'version': 'str',
        'type': 'str',
        'severity': 'str',
        'solution': 'str',
        'release': 'str',
        'rights': 'str',
        'pushcount': 'str',
        'pkglist': 'list[RpmUpdateCollection]',
        'references': 'list[dict(str, str)]'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'id': 'id',
        'updated_date': 'updated_date',
        'description': 'description',
        'issued_date': 'issued_date',
        'fromstr': 'fromstr',
        'status': 'status',
        'title': 'title',
        'summary': 'summary',
        'version': 'version',
        'type': 'type',
        'severity': 'severity',
        'solution': 'solution',
        'release': 'release',
        'rights': 'rights',
        'pushcount': 'pushcount',
        'pkglist': 'pkglist',
        'references': 'references'
    }

    def __init__(self, pulp_href=None, pulp_created=None, id=None, updated_date=None, description=None, issued_date=None, fromstr=None, status=None, title=None, summary=None, version=None, type=None, severity=None, solution=None, release=None, rights=None, pushcount=None, pkglist=None, references=None, local_vars_configuration=None):  # noqa: E501
        """RpmUpdateRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._id = None
        self._updated_date = None
        self._description = None
        self._issued_date = None
        self._fromstr = None
        self._status = None
        self._title = None
        self._summary = None
        self._version = None
        self._type = None
        self._severity = None
        self._solution = None
        self._release = None
        self._rights = None
        self._pushcount = None
        self._pkglist = None
        self._references = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        self.id = id
        self.updated_date = updated_date
        self.description = description
        self.issued_date = issued_date
        self.fromstr = fromstr
        self.status = status
        self.title = title
        self.summary = summary
        self.version = version
        self.type = type
        self.severity = severity
        self.solution = solution
        self.release = release
        self.rights = rights
        self.pushcount = pushcount
        if pkglist is not None:
            self.pkglist = pkglist
        if references is not None:
            self.references = references

    @property
    def pulp_href(self):
        """Gets the pulp_href of this RpmUpdateRecord.  # noqa: E501


        :return: The pulp_href of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this RpmUpdateRecord.


        :param pulp_href: The pulp_href of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this RpmUpdateRecord.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this RpmUpdateRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this RpmUpdateRecord.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this RpmUpdateRecord.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def id(self):
        """Gets the id of this RpmUpdateRecord.  # noqa: E501

        Update id (short update name, e.g. RHEA-2013:1777)  # noqa: E501

        :return: The id of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RpmUpdateRecord.

        Update id (short update name, e.g. RHEA-2013:1777)  # noqa: E501

        :param id: The id of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def updated_date(self):
        """Gets the updated_date of this RpmUpdateRecord.  # noqa: E501

        Date when the update was updated (e.g. '2013-12-02 00:00:00')  # noqa: E501

        :return: The updated_date of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this RpmUpdateRecord.

        Date when the update was updated (e.g. '2013-12-02 00:00:00')  # noqa: E501

        :param updated_date: The updated_date of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and updated_date is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_date`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                updated_date is not None and len(updated_date) < 1):
            raise ValueError("Invalid value for `updated_date`, length must be greater than or equal to `1`")  # noqa: E501

        self._updated_date = updated_date

    @property
    def description(self):
        """Gets the description of this RpmUpdateRecord.  # noqa: E501

        Update description  # noqa: E501

        :return: The description of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RpmUpdateRecord.

        Update description  # noqa: E501

        :param description: The description of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def issued_date(self):
        """Gets the issued_date of this RpmUpdateRecord.  # noqa: E501

        Date when the update was issued (e.g. '2013-12-02 00:00:00')  # noqa: E501

        :return: The issued_date of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._issued_date

    @issued_date.setter
    def issued_date(self, issued_date):
        """Sets the issued_date of this RpmUpdateRecord.

        Date when the update was issued (e.g. '2013-12-02 00:00:00')  # noqa: E501

        :param issued_date: The issued_date of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and issued_date is None:  # noqa: E501
            raise ValueError("Invalid value for `issued_date`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                issued_date is not None and len(issued_date) < 1):
            raise ValueError("Invalid value for `issued_date`, length must be greater than or equal to `1`")  # noqa: E501

        self._issued_date = issued_date

    @property
    def fromstr(self):
        """Gets the fromstr of this RpmUpdateRecord.  # noqa: E501

        Source of the update (e.g. security@redhat.com)  # noqa: E501

        :return: The fromstr of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._fromstr

    @fromstr.setter
    def fromstr(self, fromstr):
        """Sets the fromstr of this RpmUpdateRecord.

        Source of the update (e.g. security@redhat.com)  # noqa: E501

        :param fromstr: The fromstr of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and fromstr is None:  # noqa: E501
            raise ValueError("Invalid value for `fromstr`, must not be `None`")  # noqa: E501

        self._fromstr = fromstr

    @property
    def status(self):
        """Gets the status of this RpmUpdateRecord.  # noqa: E501

        Update status ('final', ...)  # noqa: E501

        :return: The status of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RpmUpdateRecord.

        Update status ('final', ...)  # noqa: E501

        :param status: The status of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def title(self):
        """Gets the title of this RpmUpdateRecord.  # noqa: E501

        Update name  # noqa: E501

        :return: The title of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RpmUpdateRecord.

        Update name  # noqa: E501

        :param title: The title of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def summary(self):
        """Gets the summary of this RpmUpdateRecord.  # noqa: E501

        Short summary  # noqa: E501

        :return: The summary of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this RpmUpdateRecord.

        Short summary  # noqa: E501

        :param summary: The summary of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and summary is None:  # noqa: E501
            raise ValueError("Invalid value for `summary`, must not be `None`")  # noqa: E501

        self._summary = summary

    @property
    def version(self):
        """Gets the version of this RpmUpdateRecord.  # noqa: E501

        Update version (probably always an integer number)  # noqa: E501

        :return: The version of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RpmUpdateRecord.

        Update version (probably always an integer number)  # noqa: E501

        :param version: The version of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def type(self):
        """Gets the type of this RpmUpdateRecord.  # noqa: E501

        Update type ('enhancement', 'bugfix', ...)  # noqa: E501

        :return: The type of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RpmUpdateRecord.

        Update type ('enhancement', 'bugfix', ...)  # noqa: E501

        :param type: The type of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def severity(self):
        """Gets the severity of this RpmUpdateRecord.  # noqa: E501

        Severity  # noqa: E501

        :return: The severity of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this RpmUpdateRecord.

        Severity  # noqa: E501

        :param severity: The severity of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and severity is None:  # noqa: E501
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

    @property
    def solution(self):
        """Gets the solution of this RpmUpdateRecord.  # noqa: E501

        Solution  # noqa: E501

        :return: The solution of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        """Sets the solution of this RpmUpdateRecord.

        Solution  # noqa: E501

        :param solution: The solution of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and solution is None:  # noqa: E501
            raise ValueError("Invalid value for `solution`, must not be `None`")  # noqa: E501

        self._solution = solution

    @property
    def release(self):
        """Gets the release of this RpmUpdateRecord.  # noqa: E501

        Update release  # noqa: E501

        :return: The release of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this RpmUpdateRecord.

        Update release  # noqa: E501

        :param release: The release of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and release is None:  # noqa: E501
            raise ValueError("Invalid value for `release`, must not be `None`")  # noqa: E501

        self._release = release

    @property
    def rights(self):
        """Gets the rights of this RpmUpdateRecord.  # noqa: E501

        Copyrights  # noqa: E501

        :return: The rights of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._rights

    @rights.setter
    def rights(self, rights):
        """Sets the rights of this RpmUpdateRecord.

        Copyrights  # noqa: E501

        :param rights: The rights of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rights is None:  # noqa: E501
            raise ValueError("Invalid value for `rights`, must not be `None`")  # noqa: E501

        self._rights = rights

    @property
    def pushcount(self):
        """Gets the pushcount of this RpmUpdateRecord.  # noqa: E501

        Push count  # noqa: E501

        :return: The pushcount of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._pushcount

    @pushcount.setter
    def pushcount(self, pushcount):
        """Sets the pushcount of this RpmUpdateRecord.

        Push count  # noqa: E501

        :param pushcount: The pushcount of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pushcount is None:  # noqa: E501
            raise ValueError("Invalid value for `pushcount`, must not be `None`")  # noqa: E501

        self._pushcount = pushcount

    @property
    def pkglist(self):
        """Gets the pkglist of this RpmUpdateRecord.  # noqa: E501

        List of packages  # noqa: E501

        :return: The pkglist of this RpmUpdateRecord.  # noqa: E501
        :rtype: list[RpmUpdateCollection]
        """
        return self._pkglist

    @pkglist.setter
    def pkglist(self, pkglist):
        """Sets the pkglist of this RpmUpdateRecord.

        List of packages  # noqa: E501

        :param pkglist: The pkglist of this RpmUpdateRecord.  # noqa: E501
        :type: list[RpmUpdateCollection]
        """

        self._pkglist = pkglist

    @property
    def references(self):
        """Gets the references of this RpmUpdateRecord.  # noqa: E501

        List of references  # noqa: E501

        :return: The references of this RpmUpdateRecord.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this RpmUpdateRecord.

        List of references  # noqa: E501

        :param references: The references of this RpmUpdateRecord.  # noqa: E501
        :type: list[dict(str, str)]
        """

        self._references = references

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RpmUpdateRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmUpdateRecord):
            return True

        return self.to_dict() != other.to_dict()

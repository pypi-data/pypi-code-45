# -*- coding: utf-8 -*-

"""sysdescrparser.centos."""
import re

from sysdescr import SysDescr
from utils.utils import os_version_names_regex, extract_version_number


# pylint: disable=no-name-in-module
class Centos(SysDescr):

    """Class Centos.

    SNMP sysDescr for Centos.

    """

    centos_versions = {
        "centos6": "6.0",
        "el6": "6.0",
        "centos7": "7.0",
        "el7": "7.0"
    }

    def __init__(self, raw):
        """Constructor."""
        super(Centos, self).__init__(raw)
        self.vendor = 'CENTOS'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        centos_version_names_regex = os_version_names_regex(self.__class__.centos_versions)
        centos_match = re.search(
                        centos_version_names_regex,
                        self.raw,
                        flags=re.IGNORECASE
                       )
        if not centos_match:
            return False

        self.os = "CENTOS"
        version_number = extract_version_number(
                            self.__class__.centos_versions,
                            centos_match,
                        )
        self.version = version_number

        return self

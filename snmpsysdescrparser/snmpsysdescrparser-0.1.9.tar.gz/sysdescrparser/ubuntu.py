# -*- coding: utf-8 -*-

"""sysdescrparser.ubuntu."""
import re

from sysdescr import SysDescr
from utils.utils import os_version_names_regex, extract_version_number


# pylint: disable=no-name-in-module
class Ubuntu(SysDescr):

    """Class Ubuntu.

    SNMP sysDescr for Ubuntu.

    """

    ubuntu_versions = {
        "lucid": "10.04",
        "precise": "12.04",
        "trusty": "14.04",
        "xenial": "16.04",
        "bionic": "18.04"
    }

    def __init__(self, raw):
        """Constructor."""
        super(Ubuntu, self).__init__(raw)
        self.vendor = 'CANONICAL'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        ubuntu_version_names_regex = os_version_names_regex(self.__class__.ubuntu_versions)
        ubuntu_match = re.search(
                        ubuntu_version_names_regex,
                        self.raw,
                        flags=re.IGNORECASE
                       )
        if not ubuntu_match:
            return False

        self.os = "ubuntu"
        version_number = extract_version_number(
                            self.__class__.ubuntu_versions,
                            ubuntu_match,
                         )
        self.version = version_number

        return self

# -*- coding: utf-8 -*-
"""Setup helper library specific for the runtime environment of *distutils* and *setuptools*.
"""
from __future__ import absolute_import

import os
import re
import fnmatch
import tempfile
import shutil


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "239b0bf7-674a-4f53-a646-119f591af806"

__version__ = "01.01.001"


class SetuplibError(Exception):
    pass


def help_on_user_options(uopt, uoptions, raw=False):
    """Displays the standard option data as provided by the
    "distuitls" API variable 'user_options'.

    The supported format is::

        user_options = [
            (<user-option-long>, <user-option-short>,  <user-option-description>),
            ...
        ]
    
    Args:
        uopt:
            User option::

                uopt := (
                      <user-option-long>
                    | <user-option-short>
                    | #index
                )

                user-option-long := (
                      <literal-no-args>
                    | <literal-with-hyphen-no-args>  # leading '--'
                    | <literal-with-args>    # trailing '='
                    | <literal-with-hyphen-with-args>  # leading '--' and trailing '='
                )

                user-option-short := (
                        <literal-no-hyphen>
                      | <literal-with-hyphen>  # leading '--'
                )
                
                index := int[0, length(user_options))  
                    # use for development and test only,
                    # production use is not recommended

        uoptions:
            The options definition.

        raw:
            If set to 'True', the original entry tuple is returned,
            else the formatted string for console display. 

    Results:
        Return string reference to the defined help-string. 

    Raises:
        SetupDocXError

        pass-through

    """
    _uopt = re.sub(r'^[-][-]{0,1}', r'', uopt)

    if len(_uopt) == 1:  # short-opts
        _uohelp = [x[2] for x in uoptions if x[1] == _uopt]

    else:
        # only options with arguments can have the 'help' argument
        # the long and short form too
        
        # long-opts with arguments
        _uohelp = [x for x in uoptions if x[0] == _uopt or (x[0][:-1] == _uopt and x[0][-1] == '=')]

        # if not _uohelp:
        #     # long-opts - literally
        #     _uohelp = [x for x in uoptions if x[0] == _uopt]

        if not _uohelp:
            # short-opts - literally
            _uohelp = [x for x in uoptions if x[1] == _uopt]

    if not _uohelp:
        try:
            # try as index - convert to int if required
            _uohelp = _uopt[int(uopt)]
        except:
            raise SetuplibError(
                "Unknonw option: " + str(uopt)
                )

    if raw:
        return _uohelp
    
    return "Help on Option:\n\nlong:        %s\nshort:       %s\ndescription: %s\n" %(
        str(_uohelp[0][0]), str(_uohelp[0][1]), str(_uohelp[0][2])
        )


def check_for_context_help(cmdobj, raw=False):
    """Scans for any requested context help, if present returns either a formatted
    string for console display, or the reference to the raw help entry.

    Args:
        cmdobj:
            The command object 'distutils.cmd.Command'.

        raw:
            If 'True' returns the raw entry. else a formatted
            string for console display.

    Returns:
        The help entry, either raw, or as a formatted console string.

    Raises: 
        pass-through

    """
    for o in cmdobj.user_options:
        _ax = re.sub(r'[-]', '_', o[0])
        _ax = re.sub(r'=$', '', _ax)
        if hasattr(cmdobj, _ax) and getattr(cmdobj, _ax) == 'help':
            return help_on_user_options(o[0], cmdobj.user_options)
 

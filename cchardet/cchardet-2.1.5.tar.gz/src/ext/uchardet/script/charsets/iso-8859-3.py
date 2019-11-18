#!/usr/bin/python
# -*- coding: utf-8 -*-

# ##### BEGIN LICENSE BLOCK #####
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla Universal charset detector code.
#
# The Initial Developer of the Original Code is
# Netscape Communications Corporation.
# Portions created by the Initial Developer are Copyright (C) 2001
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#          Jehan <jehan@girinstud.io>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ##### END LICENSE BLOCK #####

from codepoints import *

# ISO-8859-3 is the full 8-bit range, IANA-defined, superset of ISO/CEI 8859-3.
# It is basically the same as ISO/CEI 8859-3, but with control characters.
name = 'ISO-8859-3'
aliases = ['ISO_8859-3:1988', 'ISO_8859-3', 'iso-ir-109',
           'csISOLatin3', 'latin3', 'l3']

language = \
{
    # Languages with complete coverage.
    'complete': [ 'eo', 'tr', 'mt' ],
    'incomplete': []
}

#   X0  X1  X2  X3  X4  X5  X6  X7  X8  X9  XA  XB  XC  XD  XE  XF   #
charmap = \
[
    CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,RET,CTR,CTR,RET,CTR,CTR, # 0X
    CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR, # 1X
    SYM,SYM,SYM,SYM,SYM,SYM,SYM,SYM,SYM,SYM,SYM,SYM,SYM,SYM,SYM,SYM, # 2X
    NUM,NUM,NUM,NUM,NUM,NUM,NUM,NUM,NUM,NUM,SYM,SYM,SYM,SYM,SYM,SYM, # 3X
    SYM,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET, # 4X
    LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,SYM,SYM,SYM,SYM,SYM, # 5X
    SYM,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET, # 6X
    LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,SYM,SYM,SYM,SYM,CTR, # 7X
    CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR, # 8X
    CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR,CTR, # 9X
    SYM,LET,SYM,SYM,SYM,ILL,LET,SYM,SYM,LET,LET,LET,LET,SYM,ILL,LET, # AX
    SYM,LET,SYM,SYM,SYM,SYM,LET,SYM,SYM,LET,LET,LET,LET,SYM,ILL,LET, # BX
    LET,LET,LET,ILL,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET, # CX
    ILL,LET,LET,LET,LET,LET,LET,SYM,LET,LET,LET,LET,LET,LET,LET,LET, # DX
    LET,LET,LET,ILL,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET,LET, # EX
    ILL,LET,LET,LET,LET,LET,LET,SYM,LET,LET,LET,LET,LET,LET,LET,SYM, # FX
]

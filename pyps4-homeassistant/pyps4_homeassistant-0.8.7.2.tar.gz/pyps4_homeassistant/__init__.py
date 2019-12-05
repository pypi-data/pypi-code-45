# -*- coding: utf-8 -*-
"""Init File for pyps4_homeassistant."""
from .ps4 import *
from .connection import *
from .credential import *
from .helpers import *
from .ddp import *
from .media_art import *
from .errors import *
from .client import *

import warnings

warnings.warn("Module 'pyps4-homeassistant' has been deprecated. Use 'pyps4-2ndscreen' instead.", DeprecationWarning, stacklevel=2)

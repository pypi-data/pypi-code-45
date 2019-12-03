__version__ = '0.0.20'
__metaclass__ = type
__all__ = [
    '__init__', 'car', 'arm', 'dog', 'human', 'spider'
]
NAME = 'ddcmaker'

import platform

python_version_list = ['3.5.3']


if platform.system() == "Linux":
    from ddcmaker.linux.armv7l.makeSpider import *
    from ddcmaker.linux.armv7l.maker import *
    from ddcmaker.linux.armv7l.getip_address import *
    from ddcmaker.linux.armv7l import *
    from ddcmaker.linux.armv7l.makeros import *

else:
    from ddcmaker.confusion.maker import *


import unittest

from bgdata.configobj import BgDataInterpolation


interpolation = BgDataInterpolation({})

print('interpolating')

interpolation.interpolate('', "${PATH}")

print('done')
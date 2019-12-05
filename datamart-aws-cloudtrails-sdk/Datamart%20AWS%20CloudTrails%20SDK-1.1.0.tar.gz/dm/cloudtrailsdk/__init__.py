__author__ = 'Yaisel Hurtado <hurta2yaisel@gmail.com>'
__date__ = '15/06/18'

# pkg version are managed by setuptools_scm
# the __version__.py module will be created during build time
# also the __version__.py file is .gitignored to avoid unclean branches at build time
try:
    from .__version__ import __version__
except ImportError:
    __version__ = "0.0.0-unk.branch"

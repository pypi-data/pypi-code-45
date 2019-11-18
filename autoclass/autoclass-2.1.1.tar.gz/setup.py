"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from six import raise_from
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# *************** Dependencies *********
INSTALL_REQUIRES = ['decopatch', 'funcsigs;python_version<"3.3"', 'makefun']
DEPENDENCY_LINKS = []
SETUP_REQUIRES = ['pytest-runner', 'setuptools_scm', 'pypandoc', 'pandoc']
TESTS_REQUIRE = ['pytest', 'pytest-logging', 'PyContracts', 'enforce', 'pytypes', 'pyfields', 'valid8']
EXTRAS_REQUIRE = {'contracts': ['PyContracts'],
                  'enforce': ['enforce'],
                  'validate': ['valid8']}

# simple check
try:
    from setuptools_scm import get_version
except Exception as e:
    raise_from(Exception('Required packages for setup not found. Please install `setuptools_scm`'), e)

# ************** ID card *****************
DISTNAME = 'autoclass'
DESCRIPTION = 'Helps you write compact python classes'
MAINTAINER = 'Sylvain MARIE'
MAINTAINER_EMAIL = 'sylvain.marie@se.com'
URL = 'https://github.com/smarie/python-autoclass'
LICENSE = 'BSD 3-Clause'
LICENSE_LONG = 'License :: OSI Approved :: BSD License'

version_for_download_url = get_version()
DOWNLOAD_URL = URL + '/tarball/' + version_for_download_url

KEYWORDS = 'auto code generator getter setter constructor autoarg autoprops decorator property properties fields ' \
           'attribute attr contract object class enforce valid boilerplate pep484 type-hints runtime-typechecking ' \
           'typechecking'

with open(path.join(here, 'docs', 'long_description.md')) as f:
    LONG_DESCRIPTION = f.read()

# ************* VERSION **************
# --Get the Version number from VERSION file, see https://packaging.python.org/single_source_version/ option 4.
# THIS IS DEPRECATED AS WE NOW USE GIT TO MANAGE VERSION
# with open(path.join(here, 'VERSION')) as version_file:
#    VERSION = version_file.read().strip()
OBSOLETES = ['classtools_autocode']

setup(
    name=DISTNAME,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    # version=VERSION, NOW HANDLED BY GIT

    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,

    license=LICENSE,
    url=URL,
    download_url=DOWNLOAD_URL,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        LICENSE_LONG,

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords=KEYWORDS,

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=INSTALL_REQUIRES,
    dependency_links=DEPENDENCY_LINKS,

    # we're using git
    use_scm_version={'write_to': '%s/_version.py' % DISTNAME}, # this provides the version + adds the date if local non-commited changes.
    # use_scm_version={'local_scheme':'dirty-tag'}, # this provides the version + adds '+dirty' if local non-commited changes.
    setup_requires=SETUP_REQUIRES,

    # test
    # test_suite='nose.collector',
    tests_require=TESTS_REQUIRE,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require=EXTRAS_REQUIRE,

    obsoletes=OBSOLETES

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)

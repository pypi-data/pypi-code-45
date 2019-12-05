import os
from setuptools import find_packages, setup


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


testing_extras = [
    'coverage>=4.5.4',
    'mock>=2.0.0',
]


setup(
    name='cfgov-setup',
    version='1.3',
    py_modules=['cfgov_setup', ],
    url='https://github.com/cfpb/cfgov-django-setup',
    maintainer='CFPB',
    maintainer_email='tech@cfpb.gov',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        'distutils.setup_keywords': [
            'frontend_build_script=cfgov_setup:do_frontend_build'
        ]
    },
    extras_require={
        'testing': testing_extras,
    },
    test_suite='cfgov_setup.tests',
)

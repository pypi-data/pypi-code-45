# encoding: utf-8
"""
py_apollo 常用工具包


"""
from setuptools import setup, find_packages

SHORT = 'pyapollo from filamoon'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='py_apollo',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    url='https://github.com/filamoon/pyapollo',
    author='filamoon',
    author_email='filamoon@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    package_data={'': ['*.py', '*.pyc']},
    zip_safe=False,
    platforms='any',

    description=SHORT,
    long_description=long_description,
    long_description_content_type="text/markdown",
)

from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name = 'kvmiscs',
    version = '1.0.2',
    description = 'A Misc Functions Tools',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author = 'AnupamKris',
    author_email = 'anupamkris13262@gmail.com',
    licence = 'MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        ],  
    package = ['kvmiscs'],
    include_package_data = True,
    install_requires = ["numpy"],)
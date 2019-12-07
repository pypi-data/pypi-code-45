import setuptools
from stancmd import version

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='stancmd',
    version=version,
    description='A useless command line patience tester',
    url='https://gitlab.com/quentin-dev/stan',
    author='Quentin Barbarat',
    author_email='q.barbarat@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_namespace_packages(include=['stancmd.*']),
    install_requires=[],
    entry_points={
        'console_scripts': ['stancmd=stancmd:main'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

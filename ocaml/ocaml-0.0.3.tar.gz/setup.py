from setuptools import setup

setup(
    name='ocaml',
    version='0.0.3',
    author='Laurent Mazare',
    author_email='lmazare@gmail.com',
    packages=['ocaml'],
    package_dir={'ocaml': '.'},
    package_data={'ocaml': ['sharedlib/ocaml.so']},
    install_requires=['wurlitzer'],
)

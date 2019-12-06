from setuptools import setup


setup(
    name='big_O-dmunguiatec',
    version='0.0.1',
    description='Empirical estimation of time complexity from execution time',
    author='Pietro Berkes',
    author_email='pietro.berkes@googlemail.com',
    url='https://github.com/pberkes/big_O',
    license='LICENSE.txt',
    long_description='Please do not use this package, it is just a temporary release of a fork. Go to https://pypi.org/project/big_O/ to get the official release.',
    long_description_content_type='text/markdown',
    packages=['big_o', 'big_o.test'],
    install_requires=['numpy']
)

import setuptools

setuptools.setup(
    name='stancmd',
    version='0.2',
    description='A useless command line patience tester',
    url='https://gitlab.com/quentin-dev/stan',
    author='Quentin Barbarat',
    author_email='q.barbarat@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': ['stancmd=stan.stan:main'],
    }
)

import sys
try:
    from setuptools import setup, find_namespace_packages
except ImportError:
    print("Please upgrade pip: find_namespace_packages not found")
    sys.exit(1)

# Date-based versioning
VERSION='2019.12.04'

setup(
    name='datamaestro_ml',
    version=VERSION,
    description='Machine Learning related datasets',
    author='Benjamin Piwowarski',
    author_email='benjamin@piwowarski.fr',
    url='https://github.com/bpiwowar/datamaestro_ml',
    license='MIT',
    python_requires='>=3.5',
    packages=find_namespace_packages(include="datamaestro_ml.*"),
    package_data={
        '': [ '*.yaml' ]
    },
    install_requires=[
        'datamaestro>=0.5.1'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'datamaestro.repositories': [
            'ml = datamaestro_ml:Repository'
        ]
    },

    test_suite='datamaestro_ml.test'
)

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst', encoding='utf8') as freadme:
    readme = freadme.read()

with open('LICENSE', encoding='utf8') as flicense:
    lcns = flicense.read()

setup(
    name='nosqlmodel',
    version='1.0.0',
    description='nosqlmodel is a NoSql ORM without relations. Easy way to create models with a '
                'nosql backend. Currently Redis and Dynamodb supported.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    url='https://gitlab.com/mozgurbayhan/nosqlmodel',
    author='Mehmet Ozgur Bayhan',
    author_email='mozgurbayhan@gmail.com',
    license="BSD",
    keywords='nosql orm redis dynamo',
    # py_modules=['nosqlmodel'],
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3',
    install_requires=[
        "simplejsonobject",
        "redis",
        "botocore",
        "boto3",
    ],
    project_urls={
        'Bug Reports': 'https://gitlab.com/mozgurbayhan/nosqlmodel/issues',
        'Funding': 'https://www.losev.org.tr/bagis/Bagis.html',
        'Say Thanks!': 'https://gitlab.com/mozgurbayhan/nosqlmodel',
        'Source': 'https://gitlab.com/mozgurbayhan/nosqlmodel'
    },

    classifiers=[
        'Topic :: Database :: Front-Ends',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
    ]

)

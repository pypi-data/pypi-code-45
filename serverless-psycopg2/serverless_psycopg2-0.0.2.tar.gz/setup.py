import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='serverless_psycopg2',
    version='0.0.2',
    author='Gyeongsu Yim',
    author_email='point1304@gmail.com',
    description='psycopg2 wrapper intended to be used in aws lambda',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/point1304/serverless-psycopg2',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'psycopg2-binary>=2.8.4',
    ]
)

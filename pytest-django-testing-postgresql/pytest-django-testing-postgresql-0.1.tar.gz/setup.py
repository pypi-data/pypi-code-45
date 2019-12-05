from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pytest-django-testing-postgresql",
    version='0.1',
    description='Use a temporary PostgreSQL database with pytest-django',
    long_description=long_description,
    author='Dominik George',
    author_email='nik@naturalnet.de',
    url='https://edugit.org/nik/pytest-django-testing-postgresql',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],

    py_modules=['pytest_django_testing_postgresql'],
    install_requires=['dj-database-url', 'testing.postgresql'],
    include_package_data=True,
    zip_safe=False,

    entry_points = {
        'pytest11': [
            'django_testing_postgresql = pytest_django_testing_postgresql'
        ]
    }
)

from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='google_json_style',
    version='0.1.1',
    packages=['google_json_style'],
    url='https://gitlab.com/dmantis/google_json_style',
    license='MIT License',
    author='dmitry',
    author_email='dmitry.mantis@protonmail.com',
    description='Create Google JSON Style response bodies',
    # long_description=long_description,
    # long_description_content_type="text/markdown"
)

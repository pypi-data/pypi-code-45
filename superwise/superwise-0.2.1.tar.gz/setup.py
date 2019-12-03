from setuptools import setup
from superwise import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='superwise',
      version=__version__,
      description='Superwise SDK',
      url='https://gitlab.com/superwise.ai.docs/superwise-doc',
      author='Superwise.ai',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author_email="tech@superwise.com",
      license="MIT",
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      packages=['superwise'],
      zip_safe=False,
      python_requires='>=3.6', install_requires=['pandas', 'boto3','requests','jsonschema'])

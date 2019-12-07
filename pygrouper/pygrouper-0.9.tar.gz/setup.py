from setuptools import find_packages, setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name = "pygrouper",
    version = "0.9",
    author = "bl17zar",
    author_email = "bl17zar@gmail.com",
    description = (
        "simple realisation of cross-reference grouping "
        "algorithm; mostly used in event driven distributed systems"
    ),
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/bl17zar/pygrouper",
    packages = find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
)

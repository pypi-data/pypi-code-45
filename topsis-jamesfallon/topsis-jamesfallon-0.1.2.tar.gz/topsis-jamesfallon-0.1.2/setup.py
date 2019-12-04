import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='topsis-jamesfallon',  
    version='0.1.2',
    author="James Fallon",
    author_email="j.fallon@pgr.reading.ac.uk",
    description="Implementation of TOPSIS decision making",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/jamesfallon/topsis-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
 )

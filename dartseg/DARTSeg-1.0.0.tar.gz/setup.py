import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="DARTSeg", # Replace with your own username
    version="1.0.0",
    author="Razavian Lab",
    author_email="ark576@nyu.edu",
    description="Package for Brain Segmentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NYUMedML/DARTS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

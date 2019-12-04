import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sanau",  # Replace with your own username
    version="0.0.1",
    author="Ayazhan Zhakhan",
    author_email="az@sanau.co",
    description="Sanau package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayazhan-sanau/sanau",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

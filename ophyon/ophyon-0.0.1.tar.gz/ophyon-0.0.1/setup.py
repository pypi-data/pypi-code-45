import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ophyon",
    version="0.0.1",
    author="loading...",
    author_email= "loadin0000@example.com",
    description="for the tea ophyon static site builder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/load1n9/tea",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
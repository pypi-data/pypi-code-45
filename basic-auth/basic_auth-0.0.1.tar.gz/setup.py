import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="basic_auth",
    version="0.0.1",
    author="Rory Murdock",
    author_email="rory@itmatic.com.au",
    description="A package for read and writing auth",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/rorymurdock/basic_auth",
    packages=setuptools.find_packages(),
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)

import setuptools

with open("README.md","r") as f:
    long_description = f.read()

setuptools.setup(
    name = "Temu-Browser",
    author = "George Temu",
    author_email = "georgetemu123@gmail.com",
    description = "A browsing package",
    long_descriotion = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/pypa/sampleproject1",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-credentials", # Replace with your own username
    version="0.0.1",
    author="M S",
    author_email="po@mspcrepair.com",
    description="A simple credentials parser using a simple json file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/simple_credentials",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

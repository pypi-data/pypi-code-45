import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pwspider", # Replace with your own username
    version="2.0.1",
    author="pw",
    author_email="pangwen326@126.com",
    description="Tools for Spider",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pangwenhao326/FASTRequest/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
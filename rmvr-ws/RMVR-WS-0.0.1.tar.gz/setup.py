import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="RMVR-WS",
    version="0.0.1",
    author="V.Ramachandran",
    author_email="rama5864@gmail.com",
    description="A simple Scrapping Package",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url="https://github.com/pypa/web-scrap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", 
        ],
    python_requires='>=3.6', 
)


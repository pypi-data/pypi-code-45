import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-credentials", # Replace with your own username
    version="0.0.2",
    author="M S",
    author_email="po@mspcrepair.com",
    description="A simple credentials parser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pomaru/simple-credentials",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

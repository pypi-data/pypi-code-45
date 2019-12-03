import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coundown-pkg-mcollison", # Replace with your own username
    version="0.0.1",
    author="Matt Collison",
    author_email="m.collison@exeter.ac.uk",
    description="A simulation of the countdown game show used for demonstration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcollison/CA1-countdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

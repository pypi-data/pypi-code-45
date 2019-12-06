import setuptools

with open("README.md", "r") as fh:
    readme_contents = fh.read()

setuptools.setup(
    name = 'mlnd_distributions',
    version = '1.0',
    author = 'Anton Demurenko',
    author_email = 'dai99-uanic@priv.uanic.ua',
    description = 'Gaussian and Binomial distributions',
    long_description = readme_contents,
    long_description_content_type = "text/markdown",
    url = "https://github.com/demur/mlnd-distributions",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe = False)
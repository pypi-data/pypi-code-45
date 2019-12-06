import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-tckn-field",
    version="0.0.2",
    author="Enis B. Tuysuz",
    author_email="enisbtuysuz@gmail.com",
    description="A Django app built to integrate Republic of Turkey Identification Number to your project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enisbt/django-tckn-field",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
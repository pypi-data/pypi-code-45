
"""msQ build script for setuptools.

"""


import setuptools


with open("README.md", "r") as readme_file:
    readme_description = readme_file.read()

setuptools.setup(
    name="msQ",
    version="0.1.0.dev0",
    author="Calvin Peters",
    author_email="calvin.isotope@gmail.com",
    description="msQ",
    long_description=readme_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IsotopeC/msQ",
    packages=setuptools.find_packages(exclude=['docs', 'tests', 'examples']),
    python_requires='>3.6'
)

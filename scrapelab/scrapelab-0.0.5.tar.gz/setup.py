import setuptools
from setuptools.command.install import install
from subprocess import check_call


with open("README.md", "r") as fh:
    long_description = fh.read()


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        #check_call("scrapy startproject scrapper".split())



setuptools.setup(
    name="scrapelab", # Replace with your own username
    version="0.0.5",
    author="romio20l",
    author_email="romio20l@hotmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/romio20l/scrape_lab",
    packages=setuptools.find_packages(),
    package_data={
        'scrapelab': ['*.in']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'scrapy',
      ],
    python_requires='>=3.6',
    cmdclass={
        'install': PostInstallCommand,
    },
    include_package_data=True,
)
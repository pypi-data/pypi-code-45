
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='PyLTSpice',  
     version='0.1-post1',
     scripts=['PyLTSpice'] ,
     # install_requires = [],
     author="Nuno Brum",
     author_email="me@nunobrum.com",
     description="An set of tools to Automate LTSpice simulations",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/nunobrum/PyLTSpice",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
         "Operating System :: OS Independent",
     ],
 )
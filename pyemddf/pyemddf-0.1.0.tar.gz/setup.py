import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
#with open("requirements.txt","r") as req:
    #inst_req = req.read()
setuptools.setup(
    name='pyemddf',
    version='0.1.0',
    author='Manuel Pereira',
    author_email='afonso.pereira4525@gmail.com',
    packages=['pyemddf',],
    include_package_data=True,
    license='The MIT License',
    description='Bridge connecting python and java EMD-DF.',
    long_description=long_description,
    #install_requires=inst_req,
)
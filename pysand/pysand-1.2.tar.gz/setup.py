import pathlib
from setuptools import setup

exec(open('pysand/version.py').read())

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(name='pysand',
      version=__version__,
      description='Sand management related calculations',
      long_description=README,
      long_description_content_type="text/markdown",
      author='Thorjan Knudsvik',
      author_email='thokn@equinor.com',
      license='GNU GPL',
      url='https://github.com/equinor/pysand',
      classifiers=["Programming Language :: Python :: 3"],
      packages=['pysand'],
      install_requires=['numpy', 'scipy']
)
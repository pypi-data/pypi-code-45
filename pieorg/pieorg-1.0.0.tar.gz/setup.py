from setuptools import setup
import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(name='pieorg',
      version='1.0.0',
      description='A Python CLI app to organise every story you read on the internet.',
      long_description=README,
      long_description_content_type="text/markdown",
      author='Yash Prakash',
      author_email="yashprakash13@gmail.com",
      py_modules=['app'],
      license="MIT",
      url="https://github.com/yashprakash13/PieOrg",
      packages=["pieorg"],
      install_requires=['click', 'art'],
      entry_points='''
        [console_scripts]
        pieorg=pieorg.app:begin
    ''')

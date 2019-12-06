from setuptools import setup, find_packages

VERSION = '0.0.3'

with open('README.md', 'r', encoding="utf-8") as file:
    README = file.read()

setup(name='yl-app',
      version=VERSION,
      author="芸荳",
      author_email='yl20181003@gmail.com',
      description='a tiny cli to generate flask project',
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://gitee.com/ytxgyl/yundou-cli",
      include_package_data=True,
      # 排除.gitignore及其所在文件夹和*.pyc文件及其所在文件夹
      exclude_package_data={'': ['.gitignore', '*.pyc']},
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'yl-app=ylcli.cli:main'
          ]
      },
      classifiers=[
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ]
      )

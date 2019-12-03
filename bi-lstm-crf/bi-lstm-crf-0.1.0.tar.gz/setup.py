# encoding=utf-8

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='bi-lstm-crf',
      version='0.1.0',
      url='https://github.com/jidasheng/bi-lstm-crf',
      author='Dasheng Ji',
      author_email='jidasheng@qq.com',
      description='A PyTorch implementation of the BI-LSTM-CRF model',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='MIT',

      packages=find_packages(),

      include_package_data=True,
      install_requires=[
          "tqdm",
          "numpy",
          "pandas",
          "torch"
      ]
      )

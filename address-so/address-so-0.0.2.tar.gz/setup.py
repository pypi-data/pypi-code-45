from setuptools import setup

setup(name='address-so',
      version='0.0.2',
      description='A unified API for blockchain developers',
      url='https://github.com/address-so/address-python-sdk',
      author='Reznichenko Yaroslav',
      author_email='y@address.so',
      license='MIT',
      packages=['address'],
      install_requires=['requests>=2.20.0'],
      zip_safe=False,
      python_requires='>=3.6')

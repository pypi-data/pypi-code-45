from setuptools import setup

requires = [
    "pandas",
    "rqalpha",
]

setup(name='kdata',
      version='0.0.1',
      description='kdata.',
      url='https://github.com/jungamer/kdata',
      author='jungamer',
      author_email='624621566@qq.com',
      license='MIT',
      packages=['kdata'],
      install_requires=requires,
      zip_safe=False)

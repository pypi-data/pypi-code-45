from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='kittykittykitty',
      version='1.0',
      description='A nice kitty for your terminal',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Artistic Software',
      ],
      entry_points = {
        'console_scripts': ['kitty-lulz = kittykittykitty.lulz:main'],
      },
      keywords='programming kitty lulz wat',
      url='https://github.com/carlosgprado/PackagingTemplate',
      author='Carl OS',
      author_email='carlos.g.prado@gmail.com',
      license='MIT',
      install_requires=[
        'colorama',
      ],
      extras_require={
        'dev': [
          'pytest',
          'pytest-pycodestyle',
          'sphinx_rtd_theme',
        ]
      },
      packages=['kittykittykitty'],
      include_package_data=True,
      zip_safe=False)

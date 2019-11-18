from setuptools import setuptools

with open("README.md", "r") as fh:
      long_description = fh.read()

setuptools.setup(
      name='pxpy',
      version='1.0a10',
      author = 'Nico Piatkowski',
      author_email = 'nico.piatkowski@gmail.com',
      description = 'discrete undirected probabilistic models',
      long_description=long_description,
      url = 'https://www.randomfields.org/px',
      packages=['pxpy','pxpy.test'],
      package_data={'pxpy': ['lib/libpx.so','lib/libpx.dll','data/sin44','data/5_14.mod']},
      install_requires=['pytest','numpy','tqdm'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: Free for non-commercial use",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
      ],
      python_requires='>=3.5'
)

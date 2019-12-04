from setuptools import find_packages, setup

setup(name='andrewAudio',
      version='1.0.2',
      description='A sound-object labelling machine learning model for use with Audacity. Uses VGGish for feature extraction and a Pytorch N-way classifier neural network for training.',
      long_description_content_type="text/markdown",
      url='https://github.com/andrew-audio/andrew-model',
      author='Cooper Barth & Jack Wiig',
      author_email='cooperfbarth@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
          'pysoundfile',
          'resampy',
          'scikit-learn',
          'scipy',
          'six',
          'tensorflow',
          'torch'
      ],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ])

'''
PACKAGING:
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/* --skip-existing
'''
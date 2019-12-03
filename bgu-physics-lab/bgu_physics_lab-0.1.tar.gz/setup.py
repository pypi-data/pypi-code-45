from distutils.core import setup
from setuptools import setup, find_packages
import pathlib
setup(
  name = 'bgu_physics_lab',         # How you named your package folder (MyLib)
  # packages = ['bgu_physics_lab'],   # Chose the same as "name"
  packages=find_packages(),
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'plot and caluclate fiting goodness using chi2 regression',   # Give a short description about your library
  author = 'Adam H. Agbaria',                   # Type in your name
  author_email = 'adam.h.agb@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/AdamHamody/bgu_physics_lab',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/AdamHamody/bgu_physics_lab/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['chi2', 'regression', 'physics_lab'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'matplotlib',
          'iminuit', 'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  # package_dir={'': 'C:\\Users\\Adam Hamody Agbaria\\PycharmProjects\\LAB_2\\bgu_physics_lab'},


  include_package_data=True,

)
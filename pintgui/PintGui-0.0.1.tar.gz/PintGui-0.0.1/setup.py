from setuptools import setup

version = '0.0.1'

setup(
    name="PintGui",
    version=version,
    py_modules=['PintGui'],
    install_requires=['pint','pyside2'],
    entry_points = '''
      [gui_scripts]
      PintGui = scripts.main:start
      '''
    )

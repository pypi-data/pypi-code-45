from setuptools import setup

version = '0.0.4'

setup(
    name="PintGui",
    version=version,
    packages=['PintGui'],
    install_requires=['pint','pyside2'],
    entry_points = '''
      [gui_scripts]
      PintGui = PintGui.scripts.main:start
      '''
    )

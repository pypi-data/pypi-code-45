from setuptools import setup

version = '0.0.5'

setup(
    name="PintGui",
    version=version,
    packages=['PintGui','PintGui.scripts'],
    install_requires=['pint','pyside2'],
    entry_points = '''
      [gui_scripts]
      PintGui = PintGui.scripts.main:start
      '''
    )

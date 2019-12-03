from setuptools import find_packages,setup
setup(
    name = 'xes-lib',
    version = '0.1.1',
    author = 'xes',
    description = '学而思库',
    packages = find_packages(),
    install_requires = ["requests", "pypinyin"]
)
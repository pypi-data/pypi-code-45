from setuptools import setup, find_packages

setup(
    name = "dbg_utils",
    version = "0.0.1",
    keywords = ["pip", "pwn", "dbg"],
    description = "dbg utils for gdb",
    long_description = "...",
    license = "MIT Licence",

    author = "Lavender-Tree",
    author_email = "lavender.tree9988@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
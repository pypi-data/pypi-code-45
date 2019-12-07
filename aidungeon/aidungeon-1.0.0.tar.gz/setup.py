import os
from setuptools import setup
from setuptools import find_packages

version = "1.0.0"

setup(
    name="aidungeon",
    version=version,
    description="AI Dungeon adventure!",
    long_description="Placeholder for AIDungeon 2! Coming soon...",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="ai story dungeon game",
    url="https://github.com/nickwalton/AIDungeon",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
        ]
    },
    include_package_data=True,
    zip_safe=False,
)

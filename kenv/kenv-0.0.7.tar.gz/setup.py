from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='kenv',
    version='0.0.7',
    author='Vyacheslav Fedorov',
    author_email='fuodorov1998@gmail.com',
    description='Solver of the Kapchinsky-Vladimirsky envelope equation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fuodorov/kenv',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

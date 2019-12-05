from setuptools import setup


LONG_DESCRIPTION = """
See [mypy_boto3](https://pypi.org/project/mypy-boto3/) for more info.
"""


setup(
    name="mypy-boto3-iotsecuretunneling",
    version="1.10.33",
    packages=["mypy_boto3_iotsecuretunneling"],
    url="https://github.com/vemel/mypy_boto3",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Mypy-friendly boto3 1.10.33 type annotations for iotsecuretunneling service.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={"mypy_boto3_iotsecuretunneling": ["py.typed"]},
    install_requires=["typing_extensions; python_version < '3.8'",],
    extras_require={"master": ["mypy-boto3==1.10.33"]},
    zip_safe=False,
)

from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="summations",
    version="0.0.9.0",
    packages=["summations",],
    install_requires=[],
    license="MIT",
    url="https://github.com/reity/summations-py",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Library to enumerate all natural number "+\
                "lists with a target sum.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)

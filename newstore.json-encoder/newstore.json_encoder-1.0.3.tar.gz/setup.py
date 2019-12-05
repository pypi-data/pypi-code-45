import os

from setuptools import setup

VERSION = "1.0.3"
NAMESPACE = "newstore"
NAME = "{}.json_encoder".format(NAMESPACE)


def local_text_file(*f):
    path = os.path.join(os.path.dirname(__file__), *f)
    with open(path, "rt") as fp:
        file_data = fp.read()


setup(
    name=NAME,
    version=VERSION,
    description="JSONEncoder",
    long_description=local_text_file("README.md"),
    long_description_content_type="text/markdown",
    author="NewStore Inc.",
    author_email="dev@newstore.com",
    url="https://github.com/NewStore-oss/json-encoder",
    zip_safe=True,
    packages=[NAME],
    namespace_packages=[NAMESPACE],
    python_requires=">=3.6,<3.9",
    package_data={NAME: []},
    install_requires=["setuptools"],
)

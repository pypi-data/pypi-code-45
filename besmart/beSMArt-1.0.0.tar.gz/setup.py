from setuptools import setup, find_packages


def get_version():
    g = {}
    with open("beSMArt/version.py") as fp:
        exec(fp.read(), g)
    return g['__version__']


def readme():
    with open("README.md") as fp:
        return fp.read()


setup(
    name="beSMArt",
    version=get_version(),
    author="Patryk Niedzwiedzinski",
    author_email="pniedzwiedzinski19@gmail.com",
    description="Connect to SMA solar panel",
    long_description=readme(),
		long_description_content_type='text/markdown',
    license="MIT",
    packages=find_packages(),
    install_requires=['requests']
)

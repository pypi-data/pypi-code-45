from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="unknownannei",
    version="1.4.1",
    description="Forbidden!",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/",
    author="SaidapetSelva",
    author_email="unknownannei@unknownmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["unknownannei"],
    include_package_data=True,
        # entry_points={
    #     "console_scripts": [
    #         "weather-reporter=weather_reporter.cli:main",
    #     ]
    # },
)
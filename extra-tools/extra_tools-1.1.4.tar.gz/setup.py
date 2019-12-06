from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="extra_tools",
    version="1.1.4",
    description="A Python package for extra_tools",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nikhilkumarsingh/weather-reporter",
    author="AnupamKris",
    author_email="anupamkris13262@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["extratools"],
    include_package_data=True,
    install_requires=["requests"],
    # entry_points={
    #     "console_scripts": [
    #         "weather-reporter=weather_reporter.cli:main",
    #     ]
    # },
)
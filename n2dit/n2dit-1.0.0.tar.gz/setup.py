import setuptools
from n2dit.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="n2dit",
    version=__version__,
    author="The Deeva Authors",
    description="Deep learning-based Night-to-Day image-translation software",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/deeva/Night-to-Day-Image-translation",
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "gast==0.2.2",
        "numpy==1.16.2",
        "tensorflow-gpu==1.14",
        "matplotlib==3.1.1",
        "pillow==6.2.1",
        "opencv-python==3.4.2.17"
    ],
    entry_points={
        "console_scripts": [
            "n2dit = n2dit.__main__:main",
        ]
    })

import setuptools

with open("README.md", "r") as f:
	readme_description = f.read()

setuptools.setup(
	name="valkyrie",
	version="0.0.1",
	author="Yifan Wu",
	author_email="yw693@cornell.edu",
	description="Implementation of machine learning algorithm.",
	long_description=readme_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)

# python3 setup.py sdist bdist_wheel
# python3 -m twine upload dist/* -u kimi1994
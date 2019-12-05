import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="essay_eval",
    version="0.0.1",
    author="Sidharth Macherla",
    author_email="msidharthrasik@gmail.com",
    description="Evaluation of essays using NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SidharthMacherla/essay_eval",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",  
        "Topic :: Text Processing :: Linguistic"      
    ],
    python_requires='>=3.6',
)
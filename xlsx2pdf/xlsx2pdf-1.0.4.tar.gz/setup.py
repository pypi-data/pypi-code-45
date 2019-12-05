import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="xlsx2pdf",
    version="1.0.4",
    author="INSOFT s.r.o.",
    author_email="dosoudil@insoft.cz",
    description="Package converting xlsx spreadsheet to pdf",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
	'reportlab>=3,<4',
        'openpyxl>=3,<4'
    ]
)

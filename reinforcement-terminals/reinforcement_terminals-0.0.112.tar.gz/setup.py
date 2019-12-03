import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reinforcement_terminals", # Replace with your own username
    version="0.0.112",
    author="Samip Rai",
    author_email="samipthulung3@gmail.com",
    description="Age and Gender Detection added to module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamipThulung/reinforcement_terminals",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = ['numpy', 'Keras==2.2.4', 'tensorflow']
)




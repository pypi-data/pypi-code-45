from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()


setup(name = "allcopol",
    version = "0.1",
    description = "AllCoPol: Inferring allele co-ancestry in polyploids",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/AGOberprieler/allcopol",
    author = "Ulrich Lautenschlager",
    author_email = "ulrich.lautenschlager@ur.de",
    license = "MIT",
    packages = ["phylogen"],
    install_requires = [ 
        "argparse", "biopython", "configargparse", "numpy", "scipy"
    ],
    scripts = [
        "bin/align_clusters.py",
        "bin/allcopol.py",
        "bin/create_indfile.py",
        "bin/relabel_trees.py"
    ],
    zip_safe = False,
    python_requires = ">=3.5",
)



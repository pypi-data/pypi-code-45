import os
import re

# The function below greps and returns the name of the package stored in
# '.toml' poetry file.


def get_name_from_toml_file(workDir):

    extToml = '.toml'
    nameToml = None
    grepVersion = None
    # Search in the directory workDIr and subdirectories
    # for files with the '.toml' extension.
    for root, dirs, files in os.walk(workDir):
        for nameSearch in files:
            if nameSearch.endswith(extToml):
                nameToml = os.path.join(root, nameSearch)
    # If the toml file is found, the code searches each line
    # for a string 'name'.
    # Once the line is found, it greps the content in quotation
    # e.g. name = "some-name" --> some-name
    # If the code cannot find a file with extention '.toml' or
    # a line containing 'name', it will raise an exception.
    if nameToml is not None:
        with open(nameToml, "r") as inputFile:
            for line in inputFile:
                if "name" in line:
                    grepVersion = re.search('"(.*)"', line)
        if grepVersion is None:
            raise Exception("Cannot find package name in toml file.\n\
                 Check if the name line in toml is correctly formatted.")
        return grepVersion.group(1)
    else:
        raise Exception("Cannot find poetry .toml file")

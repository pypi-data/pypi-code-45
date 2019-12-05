from .__version__ import __version__  # noqa: F401
from pkg_resources import resource_filename
import os
import subprocess
import sys
from .get_name_from_toml_file import get_name_from_toml_file

##################################################################################################
# This function finds all the flake8 configuration files.


def flake8ConfigFiles(workDir='./'):

    pyFlake8 = None
    pyRmdFlake8 = None

    for root, dirs, files in os.walk(workDir):
        for nameSearch in files:
            if nameSearch == 'flake8_config.ini':
                pyFlake8 = os.path.join(root, nameSearch)
            if nameSearch == 'flake8_config_Rmd.ini':
                pyRmdFlake8 = os.path.join(root, nameSearch)
    return pyFlake8, pyRmdFlake8

##################################################################################################


##################################################################################################
# This function runs pytest.


def runpytests():

    runPyTest = ["pytest"] + ['-v']
    statusPyTest = subprocess.call(runPyTest)
    # processPyTest = subprocess.Popen(runPyTest, stdout=subprocess.PIPE, universal_newlines=True)
    # outputPyTest, errorPyTest = processPyTest.communicate()
    # print(outputPyTest)
    print("")
    if(statusPyTest == 1):
        print("ERROR: Pytests failed. See error details above.")
        print("")
        sys.exit(1)


####################################################################################################


####################################################################################################
# This function runs flake8 in python (.py) files.


def runflake8pythonfiles(workDir='./'):

    print("")
    print("Run flake8 in python files.")
    print("Searching for file 'flake8_config.ini'...")
    print("")
    nameFlake8ConfigFile = flake8ConfigFiles(workDir=workDir)[0]
    if nameFlake8ConfigFile is None:
        print("WARNING: Cannot find 'flake8_config.ini'." +
           " Used default flake8 configuration in jrpytests.")
        nameFlake8ConfigFile = resource_filename('jrpytests', 'flake8_config.ini')
    else:
        print("Found file 'flake8_config.ini', "
           + "using it as config file.")
    print("")

    flake8ConfFileOpt = "--config="+nameFlake8ConfigFile
    runFlake8 = ["flake8"] + [flake8ConfFileOpt]
    # Run flake8 inside python

    # statusFlake8 = subprocess.call(runFlake8)
    processFlake8 = subprocess.Popen(runFlake8, stdout=subprocess.PIPE, universal_newlines=True)
    outputFlake8, errorFlake8 = processFlake8.communicate()
    if(str(outputFlake8) != ""):
        print("Flake8 identified coding style errors in .py python files.")
        print("")
        print("List of flake8 errors in py files:")
        print(outputFlake8)
        print("")
        print("ERROR: Coding style errors in python files. See error details above.")
        print("If you want jrpytests to ignore an error, " +
           "create/modify 'flake8_config.ini' file.")
        print("")
        sys.exit(1)
    else:
        print("No python coding style errors detected in .py files.")

###################################################################################################

####################################################################################################
# This function runs flake8 in Rmarkdown python chunks. The main steps are:
# 1) Find all Rmd files in working directory.
# 2) Search python chunks in the above files.
# 3) Create temporary files where everything is commented except for python chunks.
# 4) Run flake8 on temporary files.
# 5) Print results and remove temporary files.
#
# The input is the path to the working directory (workDir).


def runflake8rmdpychunks(workDir='./', ignoreFlake8Config=False, ignoresErrors=False,
   showAllRmdFiles=False, errorListIgnored="E402,F401,E127,E128"):

    print("")
    print("Run flake8 in Rmd python chunks.")
    print("Searching for Rmd files...")
    print("")
    ################################################################################################
    # This part of the code finds all the Rmd files in working directory (workDir) and
    # its subdirectories and store the names in an array 'nameRmdFiles'.

    nameRmdFiles = []    # Array with path+name of the Rmd files

    extRmd = ".Rmd"    # Typical extension of Rmarkdown files

    # Searching for files that ends with '.Rmd' in workDir and its subdirectories,
    # and store them in the array 'nameRmdFiles' with their path from workDir.

    for root, dirs, files in os.walk(workDir):
        for nameSearch in files:
            if nameSearch.endswith(extRmd):
                # Append the search results in array 'arrRmdFiles'.
                nameRmdFiles.append(os.path.join(root, nameSearch))

    ################################################################################################
    # This part of the code loops over the Rmd files found above in search for python chunks only.

    # Initialise an array for the list of temporary files created below.

    tempNameRmdFiles = []

    # Initialise a variable with an empty string, this will be used in the loop below.

    prevLine = ""

    if showAllRmdFiles is True:
        print("List of Rmd files found in '%s'" % workDir + " and its subdirectories:")

    for name in nameRmdFiles:
        if showAllRmdFiles is True:
            print("%s\n" % name)

        # Open existing Rmd files, read-only.
        # Create new Rmd files to write in.

        with open(name, "r") as inputFile, open(name+'-CHECK', "w") as outputFile:

            # Define a flag for portions of the Rmd that are Python codes and those that are not.
            # Initialise to False.

            isPy = False

            for line in inputFile:
                if "```{python" in prevLine:
                    isPy = True
                    pyLine = prevLine
                elif line.strip() == "```":
                    isPy = False

                # If isPy is true, copy the line in the temporary file as it is,
                # if isPy is false, comment the line because it is not a Python chunk
                countSpaces = 0
                if isPy is True:
                    # Here we take into account of the fact that the entire chunk could be indented
                    # in this case, we do not want flake8 to return an error.
                    for string in pyLine:
                        if string == "`":
                            break
                        else:
                            countSpaces += 1
                    outputFile.write(line[countSpaces:])
                else:
                    outputFile.write("# # noqa "+line)  
                    # Note that "noqa" is used here to say to flake to skip errors
                    # when encountering non-python chunks.

                # This stores the line in the input file before the one considered in the loop.

                prevLine = line

        tempNameRmdFiles.append(name+'-CHECK')

    ################################################################################################
    # Run flake8 as a bash command in Python

    # List the files that should be checked by flake8.
    # Basicaly, only the temporary files generated above.

    listFlake8Files = list(tempNameRmdFiles)

    if len(listFlake8Files) > 0:

        # Add flake8 command and some configuration stuff.
        # If we choose to ignore the flake8 config file or there is no configuration file found.
        if ignoreFlake8Config is True:
            statisticsFlake8 = "--statistics"    # Print flake8 statistics
            # Errors to be ignored by flake8
            ignoreFlake8Err = "--extend-ignore="+errorListIgnored
            maxLineLengthFlake8 = "--max-line-length=100"     # Max number of characters in line

            runFlake8 = ["flake8"] + [statisticsFlake8] + [ignoreFlake8Err] + \
               [maxLineLengthFlake8] + listFlake8Files
        # Else, just use the configuration file.
        else:
            nameFlake8ConfigFilePy = flake8ConfigFiles(workDir=workDir)[0]
            nameFlake8ConfigFileRmd = flake8ConfigFiles(workDir=workDir)[1]
            print("")
            print("Searching for file 'flake8_config_Rmd.ini'...")
            print("")
            if nameFlake8ConfigFileRmd is not None:
                print("Found file 'flake8_config_Rmd.ini', "
                   + "using it as config file for flake8 in Rmd.")
                nameFlake8ConfigFile = nameFlake8ConfigFileRmd
            elif nameFlake8ConfigFileRmd is None and nameFlake8ConfigFilePy is not None:
                print("WARNING: Cannot find 'flake8_config_Rmd.ini'. Used 'flake8_config.ini'.")
                nameFlake8ConfigFile = nameFlake8ConfigFilePy
            elif nameFlake8ConfigFileRmd is None and nameFlake8ConfigFilePy is None:
                print("WARNING: Cannot find either 'flake8_config_Rmd.ini' or flake8_config.ini'." +
                   " Use default flake8 configuration in jrpytests.")
                nameFlake8ConfigFile = resource_filename('jrpytests',
                   'flake8_config.ini')
            print("")
            flake8ConfFileOpt = "--config="+nameFlake8ConfigFile
            runFlake8 = ["flake8"] + [flake8ConfFileOpt] + listFlake8Files
        # Run flake8 inside python

        # statusFlake8 = subprocess.call(runFlake8)
        processFlake8 = subprocess.Popen(runFlake8, stdout=subprocess.PIPE, universal_newlines=True)
        outputFlake8, errorFlake8 = processFlake8.communicate()
        # Remove all temporary files created above

        for tempName in tempNameRmdFiles:
            os.remove(tempName)

        if(str(outputFlake8) != ""):
            print("Flake8 identified coding style errors in Rmd python chunks.")
            print("")
            print("List of flake8 errors in Rmd files:")
            print(outputFlake8)
            print("")
            print("Note: for each line, the name of the file is displayed before '-CHECK:'")
            print("Position and nature of flake8 error is shown after '-CHECK:'")
            if ignoresErrors is False:
                print("")
                print("ERROR: Coding style errors in Rmd python chunks." +
                   " See error details above.")
                print("If you want jrpytests to ignore an error, " +
                   "create/modify 'flake8_config_Rmd.ini' file.")
                print("")
                sys.exit(1)
            else:
                print("")
                print("IgnoresErrors is set to True. Flake8 errors have been ignored.")
        else:
            print("")
            print("No python coding style errors detected in .Rmd files.")
    else:
        print("There are NO Rmd files in '%s'" % workDir + " and its subdirectories.")

    ################################################################################################

####################################################################################################

####################################################################################################
# This function checks if a directory vignettes exists in the right path.
# If so, it checks the number of pdf files in it and compares with the number of (distinct) Rmds.


def checkvignettespdffiles(workDir='./'):

    print("")
    print("Check directory 'vignettes' and pdf files in it.")
    print("Searching for directory 'vignettes'...")
    print("")
    parentDir = get_name_from_toml_file(workDir)
    ################################################################################################
    # This part of the code checks if directory vignettes exists in the right path.

    checkVignettes = False  # Flag to identify if directory 'vignettes' exists
    pathToVignettes = ''    # path+vignettes to be filled if 'vignette' exists
    # Searching for a directory called 'vignettes' in the directory parentDir.

    for root, dirs, files in os.walk(parentDir):
        for nameSearch in dirs:
            if nameSearch == 'vignettes':
                checkVignettes = True
                pathToVignettes = os.path.join(root, nameSearch)
                print("")
                print("Directory 'vignettes' exists.")
    if checkVignettes is False:
        print("")
        print("WARNING: Cannot find directory 'vignettes' in directory '%s'." % parentDir)
        print("")
    else:
        numpdfFiles = 0
        numRmdFiles = 0
        numhtmlFiles = 0
        extpdf = '.pdf'
        for roots, dirs, files in os.walk(pathToVignettes):
            for nameSearch in files:
                if nameSearch.endswith(extpdf):
                    numpdfFiles += 1

        extpdf = '.html'
        for roots, dirs, files in os.walk(pathToVignettes):
            for nameSearch in files:
                if nameSearch.endswith(extpdf):
                    numhtmlFiles += 1

        extRmd = ".Rmd"
        for root, dirs, files in os.walk(workDir):
            for nameSearch in files:
                if nameSearch.endswith(extRmd) and 'content' not in nameSearch:
                    numRmdFiles += 1
        if (numpdfFiles == numRmdFiles and numRmdFiles > 0):
            print("")
            print("Number of pdf files matches that of practical+solutions Rmd files.")
            print("")
        elif (numRmdFiles == 0):
            print("")
            print("WARNING: Cannot find Rmd files.")
            print("")
        else:
            print("")
            print("WARNING: Number of pdf files does NOT match" +
               " that of practical+solutions Rmd files.")
            print("Check if html files have been generated instead.")
            if (numhtmlFiles == numRmdFiles):
                print("")
                print("Number of html files matches that of practical+solutions Rmd files.")
                print("")
            else:
                print("ERROR: Number of pdf or html files does NOT match" +
                   " that of practical+solutions Rmd files.")
                print("")
                sys.exit(1)

    ################################################################################################

####################################################################################################

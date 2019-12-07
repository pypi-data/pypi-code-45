# import copy
import hashlib
import os
import random
# import requests
import shutil

# get tkinter for file dialogs
from tkinter import filedialog

# get downloading backbone module wget
import wget

# import other junkyard stuff
from junkyard.garbagebasket.PrintHandler import init as print_init
from junkyard.garbagebasket.PrintHandler import c_print, sl_print
from junkyard.garbagebasket.SystemHandler import handle_errors, collapse_list

handler_name = "FileHandler"

# initialize all of the outer scope variables
# standard read/write/append modes
write_modes = ("w", "write", "Write", "WRITE")
write_append_modes = ("a", "append", "Append", "APPEND")
read_modes = ("r", "read", "Read", "READ")
# TODO: do we need this?
#       do we want to add the r+ / rb+ functionality, or do the current
#       tools suffice?
read_write_modes = ("r+", "R+", "rw", "RW", "readwrite", "READWRITE")

# bytes modes
write_bytes_modes = ("wb", "WB", "w_bytes", "W_bytes")
write_append_bytes_modes = ("ab", "AB", "a_bytes", "A_bytes")
read_bytes_modes = ("rb", "RB", "r_bytes", "R_bytes")
# TODO: do we need this?
#       do we want to add the r+ / rb+ / r+b functionality, or do the current
#       tools suffice?
read_write_bytes_modes = ("rb+", "RB+", "rw_bytes", "RW_bytes")
# TODO: What about other modes like "x"?

silence = False
logging = False


def init(log=False, silent=False):
    """
    WORK IN PROGRESS

    FileHandler initializer function.
    while not required, it can be used to toggle the global variable "silence"
    which will disable all print statements within the functions

    *all functions in file can be silenced with silent=True*
    * BUT OTHERWISE HAVE INFORMATIVE PRINT STATEMENTS *

    :param log:
    :param silent: a True or False bool to determine whether or not to send print statements to console
    """
    global silence
    global logging

    if not silent and not silence:
        # do a sys.stdout.write and flush at top and bottom to print on same line
        sl_print("FileHandler() Initializing")

    silence = silent
    logging = log

    if logging:
        print_init(0)
    else:
        print_init(5)

    # if silent is false
    if not silent and not silence:
        # second stdout.write and flush to clear old message
        # and replace it with a new one
        sl_print("FileHandler() Initialized\n")


def is_directory(directory, silent=False):
    # setup help() return for the function
    """
    function to return True or False as to whether a directory exists

    :param directory: path to the directory the function will check for

    :param silent: a True or False bool to determine whether or not to make print statements

    :return: has 2 possible returns (True, False)
             True = directory exists
             False = directory does not exist
    """

    # establish function name for print/debug statements
    function_name = f"{handler_name}.is_directory()"
    silent = True if silence else silent

    # load the return of os.path.isdir() into a variable
    # to later be returned as True or False
    try:
        exists = os.path.isdir(directory)
    # account for invalid input in directory
    except TypeError:
        handle_errors(error="TypeError", log=logging, silent=silent,
                      msg=f"{function_name}: ({os.getcwd()}\\<{directory}>) triggered a TypeError in is_directory() "
                          f"- check the input")
        exists = False

    # and the directory exists
    if exists:
        # say found
        c_print(f"{function_name}: ({os.getcwd()}\\<{directory}>) found", color="GREEN", silent=silent)
    else:
        # say 'I'm sorry for the loss' -- I mean -- "not found"
        c_print(f"{function_name}: ({os.getcwd()}\\<{directory}>) not found", color="L_RED", silent=silent)
    # return the True False nature of the exists variable
    return exists


def is_file(filename, silent=False):
    # setup help() return for the function
    """
    function to return True or False as to whether a file exists

    :param filename: path to file the function will check for

    :param silent: a True or False bool to determine whether or not to make print statements

    :return: has 2 possible returns (True, False)
             True = file exists
             False = file does not exist
    """

    # establish function name for print/debug statements
    function_name = f"{handler_name}.is_file()"
    silent = True if silence else silent
    try:
        # load the True/False os.path.isfile() return into the exists variable
        # to later be returned as a file exists or file doesnt exist
        exists = os.path.isfile(filename)

        # account for invalid input in directory

    except TypeError:
        handle_errors(error="TypeError", log=logging, silent=silent,
                      msg=f"{function_name}: ({os.getcwd()}\\<{filename}>) triggered a TypeError in is_file() "
                          f"- check the input")
        exists = False

    # if file exists
    if exists:
        # say found
        c_print(f"{function_name}: ({os.getcwd()}\\<{filename}>) found", color="GREEN", silent=silent)
    # if file doesn't exist
    else:
        # say 'I'm sorry for the loss' -- I mean -- "not found"
        c_print(f"{function_name}: ({os.getcwd()}\\<{filename}>) not found", color="L_RED", silent=silent)
    # return the True False nature of the exists variable
    return exists


def file_verification(file_1, file_2, silent=False):
    """
    verifies that two files are the same file to verify file duplication success

    :param file_1:
    :param file_2:
    :param silent:
    :return:
    """
    function_name = f"{handler_name}.file_verification()"
    silent = True if silence else silent

    def hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
        for block in bytesiter:
            hasher.update(block)
        return hasher.hexdigest() if ashexstr else hasher.digest()

    def file_as_blockiter(afile, blocksize=65536):
        with afile:
            block = afile.read(blocksize)
            while len(block) > 0:
                yield block
                block = afile.read(blocksize)

    if is_file(file_1, silent=True) and is_file(file_2, silent=True):
        f_name_list = [file_1, file_2]
        file_1_hash, file_2_hash = [(f_name, hash_bytestr_iter(file_as_blockiter(open(f_name, 'rb')), hashlib.sha256()))
                                    for f_name in f_name_list]

        match = True if file_1_hash[1] == file_2_hash[1] else False
        color = "Green" if match else "L_RED"
        c_print(f"{function_name}: VERIFYING HASHES", color=color, silent=silent)
        c_print(file_1_hash[1], color=color, silent=silent)
        c_print(file_2_hash[1], color=color, silent=silent)

        # ternary conditional return, if the hashes match return true
        # and if the hashes don't match return false
        return True if match else False

    else:
        c_print(f"{function_name}: ONE OR MORE FILES DO NOT EXIST", color="L_RED", silent=silent)
        return False


# establish function name for print/debug statements
def generate_temp_filename(f_name, r_length=16, silent=False):
    # list of random characters
    function_name = f"{handler_name}.generate_temp_filename()"
    silent = True if silence else silent

    choices = ("A", "B", "C", "D", "E", "F", "G", "H",
               "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X",
               "Y", "Z", "0", "1", "2", "3", "4", "5",
               "6", "7", "8", "9")

    # generate the temp suffix
    r_suffix = [random.choice(choices) for x in range(r_length) if x is not None]
    # strip f_name list
    r_suffix = collapse_list(r_suffix)

    # create temporary file
    try:
        f_name = uniform_filename(f_name)
        extension = f".{f_name.split('.')[-1]}" if "." in f_name else ""
        temp_file = f"{f_name.split('.')[0]}{r_suffix}{extension}'" if "." in f_name else f"{f_name}{r_suffix}"
        temp_file = uniform_filename(temp_file)
        return temp_file
    except IndexError:
        handle_errors(error="IndexError", log=logging, silent=silent,
                      msg=f"{function_name}: could not generate full temporary file name, "
                          f"returning random suffix instead")
        return r_suffix


def uniform_filename(filename):
    """
    function makes filename directory strings uniform to the "\\" backslash standard

    :param filename: file directory string you want to format to a "\\" standard
    :return:
    """
    # function_name = f"{handler_name}.convert_filename()"
    filters = ["/", "//", "\\\\"]
    for f in filters:
        if f in filename:
            filename = filename.replace(f, "\\")
    return filename


def split_filename(filename, silent=False):
    # setup help() return for the function
    """
    function to split directories and file names out of file paths and return both directory and file name

    :param filename: path to the file the function will split the filename and directory from
    :param silent: a True or False bool to determine whether or not to make print statements
    :return: returns the post split filename on index[0] and directory on index[1]
    """

    # establish function name for print/debug statements
    function_name = f"{handler_name}.split_filename()"
    silent = True if silence else silent
    # if the filename contains "/"s which are a good indicator
    # that they hold a directory path
    if "/" in filename:
        # split the directory into a list separated by /'s
        new_directory = filename.split("/")
        # create a [:-value] location for the beginning of the actual filename
        # by subtracting the length of the last split against he original length
        # of the filename
        extract_index = len(filename) - len(new_directory[-1])
        directory = filename[:extract_index]
        # declare the new filename as the file index in new_directory
        filename = new_directory[-1]

    # other wise there is no directory hidden in filename, and we can just leave things as they are
    else:
        # and assign a None to directory
        directory = None

    # if not silent
    # we'll print out the returns
    c_print(f"{function_name}:", silent=silent)
    c_print(f"working directory: {os.getcwd()}", silent=silent)
    c_print(f"directory: {directory}", silent=silent)
    c_print(f"filename: {directory}", silent=silent)

    # and/or return the filename, and directory
    return filename, directory


def touch_file(filename, directory=None, mode=None, silent=False):
    # setup help() return for the function
    """
    function to create a file (and associated directories if needed) if it does
    not already exist.

    :param filename:  path to the file (may include directory) the function will create

    :param directory: OPTIONAL path to the directory containing the file

    :param mode: has 2 possible modes "w" and "wb"
                 "w" to touch a plain-text file into existence
                 "wb" to touch a bytes file into existence


    :param silent: a True or False bool to determine whether or not to make print statements

    :return: has 2 possible returns (True, False)
             True: infers that the file exists and that we were otherwise successful
             False: infers that the file not only did not exists, but continues not existing
                    and that the function has failed

    """

    # establish function name for print/debug statements
    function_name = f"{handler_name}.touch_file()"
    silent = True if silence else silent
    # check if there is a value in the directory field
    # if not we want to double check against the filename
    if directory is None:
        # call the split_filename() function and check index 0 for a filename
        # and index 1 for a directory and load them into temporary variables
        # to preserve the original filename
        temp_filename, temp_directory = split_filename(filename, silent=True)

        # we make sure that the directory that split_filename() function
        # returned isn't None, meaning it has a value, and therefore the
        # original filename had a directory in it.
        if temp_directory is not None:
            # make sure the filename is updated to reflect the split
            filename = temp_filename
            # make sure the directory is updated to reflect the split
            directory = temp_directory

            # next we want to make sure that the directory does or does not already exist
            # and create it if it doesn't using the make_directory() function
            make_directory(directory, silent=True)

        # no hidden directory so pass out to next phase
        else:
            pass

    # if there is a value in the field
    else:
        # if the directory doesn't exist, create it
        # the make_directory() function automatically checks
        # check if the directory exists first
        make_directory(directory, silent=True)

    # if there is some form of value in directory at this point
    # we should append the directory and filename together
    # at this point either way they should be split
    if directory is not None:
        filename = f"{directory}{filename}"

    # set the proper modes and content string type based on mode field argument
    # write
    if mode in write_modes:
        mode = "w"
        blank_content = ""

    # write bytes
    elif mode in write_bytes_modes:
        mode = "wb"
        # use a bytes string for write bytes
        blank_content = b""

    # if mode is None or w/e just default to write mode
    else:
        mode = "w"
        blank_content = ""

    # if the file doesn't exist
    if not is_file(filename, silent=True):
        # protect from errors -- shouldn't get them -- but we're protected if we do.
        try:
            # open it with a context manager as f and write an empty blank line based on the selected mode
            # inserting the respective string type as blank_content
            # - the context manager will automatically close the file for us <3
            with open(filename, mode) as f:
                f.write(blank_content)
        # take care of all those pesky potential errors due to potential user error
        # and return false to declare function failure
        except ValueError:
            handle_errors(error="ValueError", log=logging, silent=silent,
                          msg=f"{function_name}: ValueError with ('{filename}') as the filename, "
                              f"running in '{mode}' mode")
            return False

        except TypeError:
            handle_errors(error="TypeError", log=logging, silent=silent,
                          msg=f"{function_name}: TypeError with ('{filename}') as the filename, "
                              f"running in '{mode}' mode")
            return False

        except FileNotFoundError:
            handle_errors(error="FileNotFoundError", log=logging, silent=silent,
                          msg=f"{function_name}: FileNotFoundError with  ('{filename}') as the filename, "
                              f"running in '{mode}' mode")
            return False

        # load the bool of is_file() into a variable to determine whether or not we failed to touch the file
        exists = is_file(filename, silent=True)
        # if the file exists, we succeeded
        if exists:
            # if we're chatty cathy
            if not silent and not silence:
                # say "we rule, the genes are on top of shit, we won, everything is good and nothing is bad"
                c_print(f"{function_name}: successfully touched ({os.getcwd()}\\<{filename}>)", color="GREEN")

        # if the file doesn't exist
        else:
            # and we're talking
            if not silent and not silence:
                # say "we suck, and failed a simple task... that we are failures -- just like the ancestors"
                # let them know that this failure is not only a programmatic failure but also a genetic one
                c_print(f"{function_name}: failed to touch ({os.getcwd()}\\<{filename}>)", color="RED")

        # and/or return the exists bool to represent success or failure
        return exists

    # if the file already exists, skip the whole song and dance and write home about it
    else:
        # if we can talk
        if not silent and not silence:
            # we will talk, we'll tell them how their precious file already exists
            c_print(f"{function_name}: ({os.getcwd()}\\<{filename}>) already exists", color="YELLOW")

            # we will return a True value because the file existing, is functionally
            # the same as successfully touching the file
            return True


def make_directory(directory, silent=False):
    # setup help() return for the function
    """
    function to CREATE NEW DIRECTORIES if they don't already exists

    :param directory: path to the directory the function is creating

    :param silent: a True or False bool to determine whether or not to make print statements

    :return: has 2 possible return values of True and False (bool)
             True: The directory was successfully created, or otherwise already exists
                   both are functionally the same
             False: The directory does not exist, or the function was otherwise unable to
                    create the directory
    """

    # establish function name for print/debug statements
    function_name = f"{handler_name}.make_directory()"
    silent = True if silence else silent
    # if the file exists pass
    if is_directory(directory, silent=True):
        # if silent == false
        if not silent and not silence:
            # let them know that the directory exists and that there is no need
            # to create it
            c_print(f"{function_name}: could not create the directory ({os.getcwd()}\\<{directory}>)")
            c_print("because it already exists")

        # we'll return with a True, to say that YES the directory is there
        # even though *this function* didn't create it.
        # the goal of having the directory exist is still met.
        return True

    # otherwise create the directory
    else:
        # attempt to create the directory using os.makedirs()
        try:
            os.makedirs(directory)
        # if TypeError
        except TypeError:
            handle_errors(error="TypeError", log=logging, silent=silent,
                          msg=f"{function_name}: ({os.getcwd()}\\<{directory}>) triggered a TypeError in "
                          f"make_directory({directory}) -- check input")
            return False

        # if ValueError
        except ValueError:
            handle_errors(error="ValueError", log=logging, silent=silent,
                          msg=f"{function_name}: ({os.getcwd()}\\<{directory}>) triggered a ValueError in"
                          f" make_directory({directory}) -- check input")
            # return False to state that the function failed
            return False
        # check if the directories were successfully created and return the bool into a variable
        exists = is_directory(directory, silent)
        # use the exists bool to determine how we continue
        # if directories were successfully created
        if exists:
            c_print(f"{function_name}: ({os.getcwd()}\\<{directory}>) was successfully created!",
                    color="GREEN", silent=silent)
        # if directories were unsuccessfully created
        else:
            # let them know that it was a failure
            c_print(f"{function_name}: failed to create ({os.getcwd()}\\<{directory}>) as a directory",
                    color="RED", silent=silent)

        # return the bool to determine success or failure
        return exists


def read_file(filename, mode=None, silent=False):
    # setup help() return for the function
    """
    function to READ return the contents of a file

    :param filename: path to the file the function is reading

    :param mode: has 3 possible modes ('r', 'rb', 'None')
                 'None' - Attempts to decide the read mode automatically (Experimental)
                 'r'    - reads the file in 'r' (plain text) mode
                 'rb'   - reads the file in 'rb' (bytes) mode

    :param silent: a True or False bool to determine whether or not to make print statements

    :return: has 2 possible returns (Content, None)
             the function should return the content of the file
             or if an error is encountered along the way
             it will return None
    """

    # establish function name for print/debug statements
    function_name = f"{handler_name}.read_file()"
    silent = True if silence else silent
    if is_file(filename, silent=True):
        # set mode accordingly
        # TODO: Investigate additional read modes
        # read plain
        if mode in read_modes:
            mode = "r"
        # read bytes
        elif mode in read_bytes_modes:
            mode = "rb"

        # if the mode is None / unfilled
        elif mode is None:
            #       INCLUDE AUTOMATIC PROCESSING DURING "mode=None" CALLS
            #       -- ENDED UP TAKING A DIFFERENT APPROACH, WE USE TRY/EXCEPT TYPEERROR
            #          TO CATCH IF WE HAVE THE WRONG MODE, IF WE DO WE TRY THE OTHER READ
            #          MODE.
            #          HOPING THIS WORKS!
            #       -- (SEEMS TO BE WORKING)

            try:
                with open(filename, "r") as f:
                    return f.read()
            except TypeError:
                with open(filename, "rb") as f:
                    return f.read()

        # use a context manager to open the file and return its contents
        # the context manager will automatically close the file once
        try:
            with open(filename, mode) as f:
                return f.read()
        # handle pesky errors that may arise for whatever reason and inform the user
        # and then pass out of the function, returning None
        except ValueError:
            handle_errors(error="ValueError", log=logging, silent=silent,
                          msg=f"{function_name}: ValueError with ('{filename}') as the filename, "
                              f"running in '{mode}' mode")
            return None
        except TypeError:
            handle_errors(error="TypeError", log=logging, silent=silent,
                          msg=f"{function_name}: TypeError with ('{filename}') as the filename, "
                              f"running in '{mode}' mode")
            return None

    # if the file doesn't
    else:
        # if we can tell secrets
        # announce it to the world
        c_print(f"{function_name}: file not found.", color="L_RED", silent=silent)
        # and return None to represent the file doesn't exist
        return None


# TODO: INCREASE SAFETY OF THE WRITE FUNCTION BY USING A TEMP FILE (DONE)
def write_file(content, filename, mode=None, encoding='utf-8', overwrite=False, verify_write=True, silent=False):
    # setup help() return for the function
    """
    function to WRITE FILES

    :param content: content to write to the file

    :param filename: path to the file the function is writing

    :param mode: write mode, comes in two 5 flavors, write, writebytes, append, appendbytes, and None
                 None(Default) mode - will determine if the file exists and make it if it doesn't
                                      and determine from the content type whether or not to write
                                      in bytes or plain modes.  --  this is essentially an automatic
                                      mode.

                 "w" (write) mode - will write the file as a plain text with a new line at the end
                                    !CAUTION! - THIS WILL WIPE THE FILE'S PREVIOUS CONTENTS, IF ANY
                                                AND REPLACE IT WITH THE CONTENTS OF THE CONTENT FIELD

                 "wb" (write bytes) mode - this mode is a lot like "w" mode except it writes in bytes
                                           without a new line, but carries the same content wiping
                                           warning as "w" mode.

                 "a" (append) mode - this mode should be used on existing files, and will add the "content" field
                                     to the last line of a plain text type file (such as .txt)

                 "ab" (append bytes) mode - this mode is meant to add bytes type content directly to the end
                                            of a bytes file (such as .jpg, or other data type) :shrug:

    :param encoding: encoding used for bytes mode -- example usage: 'utf-8'

    :param silent: a True or False bool to determine whether or not to make print statements

    :param overwrite: whether to overwrite or not

    :param verify_write: check md5 checksum of temporary file and target file before removing the temporary file

    :return: (True, False) bool return to confirm that the file exists at end of function
             if it returns false it means that the write has somehow failed.
    """

    function_name = f"{handler_name}.write_file()"
    silent = True if silence else silent

    # we'll set the modes to their proper values based on the user's call
    # and assign the proper content type
    # set mode to standard write
    if mode in write_modes:
        mode = "w"
        # create a new line each entry
        content = f'{content}\n'

    # set mode to write bytes
    elif mode in write_bytes_modes:
        mode = "wb"
        # make sure the data is bytes type and give it an encoding
        if isinstance(content, bytes):
            pass
        else:
            content = bytes(content, encoding=encoding)

    # set mode to append standard
    elif mode in write_append_modes:
        mode = "a"
        # create a new line each entry
        content = f'{content}\n'

    # set mode to append bytes
    elif mode in write_append_bytes_modes:
        mode = "ab"
        # make sure the data is bytes type and give it an encoding
        if isinstance(content, bytes):
            pass
        else:
            content = bytes(content, encoding=encoding)

    # if the mode field argument is empty
    if mode is None:
        # if the file exists
        if is_file(filename, silent=True):
            # and is_bytes is set to zero
            if isinstance(content, bytes):
                # set to append bytes
                mode = "ab"
            # if the content isn't bytes
            else:
                # set to append (plain txt)
                mode = "a"
                # set content to string() type
                content = f'{content}\n'
        # if the file doesnt exist
        else:
            # and is_bytes is set to zero
            if isinstance(content, bytes):
                # set to write bytes
                mode = "wb"
            # if is_bytes is anything but 0
            else:
                # set to write (plain txt)
                mode = "w"
                # set content to string() type
                content = f'{content}\n'

    # let's make sure that we don't get any errors
    # TODO: MAKE SAFE WRITE WITH TEMP FILE (DONE, refine?) (UPDATE COMMENTS!)
    temporary_file = generate_temp_filename(filename)
    try:
        # create a temporary file and if in append mode
        # copy content of existing file (if it exists) into the temporary file
        # and then write content to the temporary file

        # for appending
        # if the file exists copy it as the base for the temporary file
        if is_file(filename, silent=True):
            if mode in ("a", "ab"):
                copy_file(filename, temporary_file, mode="copy2", overwrite=overwrite, silent=True)

        # write the content to the temp file (append if in append mode)
        with open(temporary_file, mode) as outfile:
            outfile.write(content)

    # such as value errors or...
    except ValueError:
        handle_errors(error="ValueError", log=logging, silent=silent,
                      msg=f"{function_name}: ValueError with ('{filename}') as the filename, running in '{mode}' mode")
        return False
    # type errors
    except TypeError:
        handle_errors(error="TypeError", log=logging, silent=silent,
                      msg=f"{function_name}: TypeError with ('{filename}') as the filename, running in '{mode}' mode")
        return False
    # permission errors
    except PermissionError:
        handle_errors(error="PermissionError", log=logging, silent=silent,
                      msg=f"{function_name}: PermissionError with ('{filename}') as the filename, "
                          f"running in '{mode}' mode")
        return False

    # after we finish the temp_file write we can return whether or not the file
    # was successfully created using the is_file() function
    temp_exists = is_file(temporary_file, silent=True)
    if temp_exists:
        # check to see if the current file already exists
        # delete the original file
        # copy the temporary_file to the filename
        copy_file(temporary_file, filename, mode="copy2", overwrite=True, silent=True)
        # remove the temporary file if it and the target file exist
        if is_file(temporary_file, silent=True) and is_file(filename, silent=True):
            # if verify_write is true then get the sha256 returns of both the temporary file
            # and the target file and compare them, if they are not the same, do not delete
            # the temporary file
            if verify_write:
                # TODO: Verification Function (DONE)
                if file_verification(temporary_file, filename, silent=True):
                    remove_file(temporary_file, silent=True)
                    if is_file(temporary_file, silent=True):
                        c_print(f"{function_name}: failed to automatically remove the temporary file",
                                color="L_RED", silent=silent)
                    else:
                        c_print(f"{function_name}: successfully removed the temporary file",
                                color="GREEN", silent=silent)

                else:
                    c_print(f"{function_name}: failed to write file.", color="RED", silent=silent)
                    c_print(f"your data can be recovered from {temporary_file}", color="L_RED", silent=silent)
                    return False
            else:
                remove_file(temporary_file, silent=True)
                if is_file(temporary_file, silent=True):
                    c_print(f"{function_name}: failed to automatically remove the temporary file",
                            color="RED", silent=silent)
                    c_print(f"{split_filename(temporary_file)[1]}", color="L_RED", silent=silent)
                    return False
                return True
        else:
            c_print(f"{function_name}: failed to write the temporary file file.", color="RED", silent=silent)
            return False

        # after we finish the write we can return whether or not the file
        # was successfully created using the is_file() function
        exists = is_file(filename, silent=True)

        # if the file exists
        if exists:
            c_print(f"{function_name}: successfully wrote {filename} in '{mode}' mode",
                    color="GREEN", silent=silent)
        else:
            c_print(f"{function_name}: failed to write {filename} in '{mode}' mode", color="RED", silent=silent)
        return exists

    else:
        c_print(f"{function_name}: failed to write {temporary_file} in '{mode}' mode", color="RED", silent=silent)
        return False


def remove_directory(directory, mode="single", silent=False):
    # setup help() return for the function
    """
    function to REMOVE DIRECTORIES

    :param directory: path to the directory the function is removing

    :param mode: function has 3 modes ("single", "all", and "clear")
                "single" mode - removes the end point target directory, ( will not remove files )

                "all" mode - removes all directories between the working directory
                             and the target directory. ( will not remove files)

                "clear" mode - removes a directory and all of its children
                               !! CAUTION YOU WILL LOSE ALL CONTENT UNDER THE TARGET DIRECTORY!!


    :param silent: a True or False bool to determine whether or not to make print statements

    :return: the function has 3 possible returns
             (True, False, None)
             True = Directory Removed
             False = Directory Removal Failed
             None = Directory Does Not Exist

    """

    # establish function name for print/debug statements
    function_name = f"{handler_name}.remove_directory()"
    silent = True if silence else silent

    # we'll just take a bit of code from the remove_file() function and turn it into
    # a reusable sub function to confirm the success of the main function, across modes
    def confirm_remove(sf_directory):
        # use the is_directory to determine whether or not we successfully deleted the directories
        # and return a bool for success/failure
        _exists = is_directory(sf_directory, silent=True)
        if _exists:
            c_print(f"{function_name}: ({os.getcwd()}\\<{sf_directory}>) unsuccessfully removed",
                    color="L_RED", silent=silent)
        # if the file still exists the function has failed remove it
        else:
            c_print(f"{function_name}: ({os.getcwd()}\\<{sf_directory}>) successfully removed",
                    color="GREEN", silent=silent)
        # return the bool exists to determine success or failure
        return _exists

    # begin function logic
    # check if the directory exists
    if is_directory(directory, silent=True):
        # and filter modes between single and all

        # "single" mode deletes the end directory only.
        if mode == "single":
            # make sure that the file directory is empty
            try:
                # use the os.rmdir() function to remove the directory
                os.rmdir(directory)

                # return whether or not the directory was deleted
                # by using the sub function
                return confirm_remove(directory)

            # if we except with an OSError, it means that the directory has contents
            except OSError:
                # if silent set to !FALSE! ( ͡ʘ ͜ʖ ͡ʘ) *slowly unwinds*
                # blah blah blah
                c_print(f"{function_name}: ({os.getcwd()}\\<{directory}>) is not empty\n"
                        f"Consider using 'clear' mode to remove the target directory, "
                        f"and all sub-directories/files",
                        color="L_RED", silent=silent)
                # and/or return as False, directory could not be removed.
                return False

        # "all" mode removes all directories between the working directory and the target directory
        elif mode == "all":
            # make sure that the file directory is empty with try/except statement
            try:
                # call os.removedirs() with the directory passed in to remove all
                # directories between working and target
                os.removedirs(directory)

                # return whether or not the directory was deleted
                # by using the sub function
                return confirm_remove(directory)

            # if we except with an OSError, it means that the directory has contents
            except OSError:
                # squaaawwwk!!
                c_print(f"{function_name}: ({os.getcwd()}\\<{directory}>) is not empty\n"
                        f"Consider using 'clear' mode to remove the target directory, "
                        f"and all sub-directories/files",
                        color="L_RED", silent=silent)
                # and/or return as False, directory could not be removed.
                return False

        # "clear" mode removes everything under a target directory
        elif mode == "clear":
            # using the shutil.rmtree(directory) function.
            shutil.rmtree(directory)

            # let's check that the directory has been deleted
            exists = is_directory(directory, silent=True)
            # FAILURE
            if exists:
                c_print(f"{function_name}: could not clear ({os.getcwd()}\\<{directory}>)",
                        color="RED", silent=silent)

            # SUCCESS
            else:
                c_print(f"{function_name}: successfully cleared ({os.getcwd()}\\<{directory}>) and "
                        f"all sub-directories/files", color="GREEN", silent=silent)
            # we return the True False bool of exists to indicate success or failure.
            return exists

    # if the directory doesn't exist
    else:
        # let the user know that the directory doesn't exist.
        c_print(f"{function_name}: could not remove ({os.getcwd()}\\<{directory}>)", color="RED", silent=silent)
        c_print(f"directory does not exist!", color="L_RED", silent=silent)
        # return that the directory is None (Does Not Exist)
        return None


# TODO: add secure delete with some sort of looped overwrite function?  Need to research before diving
#       into this one.
def remove_file(filename, silent=False):
    # setup help() return for the function
    """
    function to REMOVE FILES

    :param filename: path to the file the function is removing

    :param silent: a True or False bool to determine whether or not to make print statements

    :return: has 3 possible returns (True, False, None)
             (True, False, None)
             True = File Removed
             False = File Removal Failed
             File Does Not Exist
    """

    # establish function name for print/debug statements
    function_name = f"{handler_name}.remove_file()"
    silent = True if silence else silent
    # silently make sure the file exists
    if is_file(filename, silent=True):
        # if the file exists use the imported os module to remove it
        try:
            os.remove(filename)
        except PermissionError:
            pass

        # use the is_file to determine whether or not we successfully deleted the file
        # and return a bool for success/failure
        if not is_file(filename, silent=True):
            c_print(f"{function_name}: ({os.getcwd()}\\<{filename}>) successfully removed",
                    color="GREEN", silent=silent)

            # and/or return that we have removed the file
            return True

        # if the file still exists the function has failed remove it
        else:
            c_print(f"{function_name}: ({os.getcwd()}\\<{filename}>) unsuccessfully removed",
                    color="RED", silent=silent)

            # and/or return that we have failed to remove the file
            return False

    # if the file doesn't exist...
    else:
        # if not silent, let the user know that the file doesn't exist.
        if not silent and not silence:
            # if the file doesnt exist, then run away screaming and crying
            c_print(f"{function_name}: could not remove ({os.getcwd()}\\<{filename}>)", color="RED", silent=silent)
            c_print(f"file does not exist.", color="L_RED", silent=silent)

        # and/or return that the file is None (Does Not Exist)
        return None


def get_all_file_dirs(starting_dir, silent=False):
    """
    function to grab all file pointer directories under a target directory
    and return the output as a list of strings

    :param starting_dir: the directory under which to find all file directories
    :param silent: whether or not to print
    :return: list of file directories
    """
    """"""
    # function name
    function_name = f"{handler_name}.filter_dirs()"
    silent = True if silence else silent

    # sub function to sort to output
    def process_output(f_path, out):
        if os.path.isdir(f_path):
            out = out + get_all_file_dirs(f_path)
        else:
            out.append(f_path)
        return out

    # handle errors
    try:
        # create a list of file and sub directories
        # names in the given directory
        list_of_files = os.listdir(starting_dir)
        output = []
        # Iterate over all the entries
        for entry in list_of_files:
            # Create full path
            full_path = os.path.join(starting_dir, entry)
            # If entry is a directory then get the list of files in this directory
            # using the process_output() sub-function
            output = process_output(full_path, output)

        # return the output
        return output
    # if access denied
    except PermissionError:
        handle_errors(error="PermissionError", log=logging, silent=silent,
                      msg=f"{function_name}: {function_name}: AccessDenied")
    # if file not found
    except FileNotFoundError:
        handle_errors(error="FileNotFoundError", log=logging, silent=silent,
                      msg=f"{function_name}: {function_name}: File Not Found!")


def filter_dirs(dir_list, extension=None):
    """
    function to return an optionally filtered list of file pointer directories
    returned by the get_all_file_dirs() function

    :param dir_list: a list of directories to filter and pass
    :param extension: a .abc extension filter, only returns files with specified extension
    :return: returns a list comprehension of (optionally extension filtered) file directories
    """
    # function name
    function_name = f"{handler_name}.filter_dirs()"
    # handle potential errors
    try:
        # if the extension argument is is unfilled
        if extension is None:
            # we'll just return the dir_list
            return dir_list
        # otherwise
        else:
            # we will return a list comprehension that only contains file pointers that
            # contain the .extension argument string
            return [directory for directory in dir_list if extension in directory]
    #
    # type error
    except TypeError:
        return f"{function_name}: TypeError"


def print_dirs(dir_list, mode="normal", silent=False):
    """
    function that prints a line spaced directories -- or can (optionally) print them
    as a formatted 'list'-alike set of strings that can be copied and pasted into code

    :param dir_list: list of strings containing directories
    :param mode: (normal, formatted)
                    normal - print line spaced and stripped of container clutter
                    formatted - made to look like a python code formatted
                                line separated list
    :param silent: whether or not to print
"""
    # do a before loop conditional
    # to check the mode
    if mode == "formatted":
        # and make a decorative print to kick off the output before the loop begins
        c_print("f_dir_list = ")

    # enumerate the dir_list to get the index and file pointer strings
    for index, system_link in enumerate(dir_list):
        # make sure the item in the list is a string otherwise pass around for the next loop
        if isinstance(system_link, str):
            if mode == "normal":
                c_print(system_link)
            elif mode == "formatted":
                # slice the system_link so that the output is usable in code
                s_link = system_link.replace("/", "\\")
                s_link = s_link.replace("\\", "\\\\")

                # handle index positions to craft a list like console output using the print statement
                # handling the first line
                if index == 0:
                    c_print(f"['{s_link}',", silent=silent)

                # all in-between lines
                elif index + 1 < len(dir_list):
                    c_print(f" '{s_link}',", silent=silent)

                # and the last line
                else:
                    c_print(f" '{s_link}']", silent=silent)


def copy_file(src_file, dest_file=None, mode="copy", overwrite=False, silent=False):
    """
    function to copy individual files into a new directory with an optionally formatted name

    :param src_file: file to be copied
    :param dest_file: destination of copied file
    :param mode: shutils -- (copy, copy2, copyfile)
    :param overwrite: whether or not to delete the original file and try again when confronted with a FileExistsError
    :param silent: whether or not to print debug statements
    :return: 
    """
    # function name
    function_name = f"{handler_name}.copy_file()"
    silent = True if silence else silent
    # possible mode calls
    copy_mode = (1, "c", "C", "copy", "Copy", "COPY")
    copy2_mode = (2, "c2", "C2", "copy2", "Copy2", "COPY2")
    copyfile_mode = (3, "cf", "Cf", "CF", "copyfile", "Copyfile", "CopyFile", "COPYFILE")

    # sub function to do all the work
    def c_file(s_file, d_file, _mode):

        failure = False
        if _mode in copy_mode:
            try:
                # try to copy the file
                shutil.copy(s_file, d_file, follow_symlinks=True)
            except FileNotFoundError:
                failure = handle_errors("FileNotFoundError", silent=silent)
            except PermissionError:
                failure = handle_errors("PermissionError", silent=silent)
            except FileExistsError:
                if not overwrite:
                    failure = handle_errors("FileExistsError", silent=silent)
                # if file exists and is set to overwrite remove the file in the way
                # and try again
                else:
                    remove_file(dest_file)
                    c_file(src_file, dest_file, _mode)
            except OSError:
                failure = handle_errors("OSError", silent=silent)

        elif mode in copy2_mode:
            try:
                shutil.copy2(src_file, dest_file, follow_symlinks=True)
            except FileNotFoundError:
                failure = handle_errors("FileNotFoundError", silent=silent)
            except PermissionError:
                failure = handle_errors("PermissionError", silent=silent)
            except FileExistsError:
                if not overwrite:
                    failure = handle_errors("FileExistsError", silent=silent)
                # if file exists and is set to overwrite remove the file in the way
                # and try again
                else:
                    remove_file(dest_file)
                    c_file(src_file, dest_file, _mode)
            except OSError:
                failure = handle_errors("OSError", silent=silent)

        elif mode in copyfile_mode:
            try:
                shutil.copyfile(src_file, dest_file, follow_symlinks=True)
            except FileNotFoundError:
                failure = handle_errors("FileNotFoundError", silent=silent)
            except PermissionError:
                failure = handle_errors("PermissionError", silent=silent)
            except FileExistsError:
                if not overwrite:
                    failure = handle_errors("FileExistsError", silent=silent)
                # if file exists and is set to overwrite remove the file in the way
                # and try again
                else:
                    remove_file(dest_file)
                    c_file(src_file, dest_file, _mode)
            except OSError:
                failure = handle_errors("OSError", silent=silent)

        else:
            failure = handle_errors("ModeError", silent=silent)

        if is_file(dest_file, silent=True) and not failure and file_verification(src_file, dest_file, silent=True):
            c_print(f"{function_name}: successfully copied\nfrom:({src_file})\nto: ({dest_file})",
                    color="GREEN", silent=silent)
        else:
            c_print(f"{function_name}: something went wrong while copying:\nfrom:({src_file})\nto: ({dest_file})",
                    color="RED", silent=silent)

    if dest_file is None:
        dest_file = filedialog.askdirectory()
        dest_file = uniform_filename(dest_file)

    # run sub-function
    c_file(src_file, dest_file, mode)


def mass_copy(file_list, dest_dir=None, mode="c", silent=False):
    """
    function to copy an entire list of files into a single directory

    :param file_list: list or tuple containing file pointing directories
    :param dest_dir: destination directory to copy the list of files
    :param mode: to copy in c, c2, cfile (shutil.copy/copy2/copyfile)
    :param silent: whether or not to print statements
    """
    function_name = f"{handler_name}.mass_copy()"
    silent = True if silence else silent

    copy_mode = (1, "c", "C", "copy", "Copy", "COPY")
    copy2_mode = (2, "c2", "C2", "copy2", "Copy2", "COPY2")
    copyfile_mode = (3, "cf", "Cf", "CF", "copyfile", "Copyfile", "CopyFile", "COPYFILE")

    if dest_dir is None:
        dest_dir = filedialog.askdirectory()
        dest_dir = uniform_filename(dest_dir)

    for index, system_link in enumerate(file_list):
        if mode in copy_mode or mode in copy2_mode or mode in copyfile_mode:
            # c_print(f"copying {system_link} to {dest_dir} in {mode}")
            try:
                copy_file(system_link, dest_dir, mode)
            except ValueError:
                handle_errors(error="ValueError", log=logging, silent=silent)
            except TypeError:
                handle_errors(error="TypeError", log=logging, silent=silent)

        else:
            c_print(f"{function_name}: copy mode out of range; defaulting to copy mode", color="L_RED", silent=silent)
            copy_file(system_link, dest_dir, "c", silent=silent)


def download_file(file_url, extension=None, directory=None, silent=False):
    """

    :param file_url:
    :param extension:
    :param directory:
    :param silent:
    :return:
    """

    function_name = f"{handler_name}.download_file()"
    silent = True if silence else silent
    failure = False

    # def bar_custom(current, total, width=80):
    #     if not silent:
    #         sl_print(f"Downloading: {current / total * 100:.2f} [{current} / {total}] bytes")

    if directory == "gui":
        file_name = filedialog.asksaveasfilename()
        file_name = uniform_filename(file_name)
    else:
        # set up directory if applicable
        if directory:
            directory = uniform_filename(directory)

        # clean up url name to get file name
        file_name = file_url.split('/')[-1]
        # append .file extension to filename
        if "." not in file_name and extension:
            extension_separator = "." if "." not in extension else ""
            file_name = f'{file_name}{extension_separator}{extension}'

        # append directory if applicable
        if directory is not None:
            file_name = f"{directory}\\{file_name}" \
                if directory[-1] != "\\" and directory[-1] != "\\\\" and directory[-1] != "/" \
                else f"{directory}{file_name}"

    if not silent:
        sl_print(f"{function_name}: downloading {file_url} to {file_name}")
    # download file
    wget.download(file_url, out=file_name)

    if is_file(file_name, silent=True) and not failure:
        if not silent:
            sl_print(f"{function_name}: successfully downloaded {file_url} to {file_name}\n")
    else:
        if not silent:
            sl_print(f"{function_name}: unsuccessfully downloaded {file_url} to {file_name}\n")


if __name__ == '__main__':
    test_file = "https://freesound.org/data/previews/12/12691_32572-lq.mp3"
    download_file(test_file, directory="gui")

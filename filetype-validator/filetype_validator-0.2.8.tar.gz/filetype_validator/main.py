import filetype
import os
from .extension_definition import matching_extensions
from io import BufferedReader

def reset_pointer(file_object):
    # return read pointer to initial so buffered reader object 
    # can be re-read on caller side
    file_object.seek(0)

def determine_extension(file_object):
    file_name = ""
    try:
        # first try to extract filename from FileStorage or 
        # BufferedReader object
        if type(file_object) == BufferedReader:
            file_name = file_object.name
            reset_pointer(file_object)
        elif type(file_object) == str:
            file_name = os.path.basename(file_object)
        else:
            # try from werkzeug FileStorage
            file_name = file_object.filename
            reset_pointer(file_object)
    except AttributeError:
        # Take no action for now
        pass
    
    file_ext = os.path.splitext(file_name)[-1]
    # extension should always in lowercase to match with return from 
    # filetype.py detection
    return file_ext.replace(".", "").lower()

def compare(file_extension, detected_extension):
    # only check files that have extensions 
    # check matching extensions for detected type
    if file_extension and file_extension != detected_extension:
        return file_extension in matching_extensions.get(detected_extension, [])
    
    return True

def validate(file_object):
    # get mime type from header signature information
    # extensions for corresponsing header signature reference
    # https://en.wikipedia.org/wiki/List_of_file_signatures
    file_extension = determine_extension(file_object)
    detected_extension = filetype.guess_extension(file_object)

    return compare(file_extension, detected_extension)
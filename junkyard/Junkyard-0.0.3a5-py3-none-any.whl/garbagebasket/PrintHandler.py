import datetime
import os
import sys

verbose = 0
initialized = False

try:
    # import colorama
    import colorama
except ImportError:
    print("PrintHandler -- could not import colorama -- color function will be disabled")
    colorama = None


def init(verbosity=0):
    """
    Initializes colorama and adjusts log verbosity level

    :param verbosity: control the print level when log_mode is set
                      0 - Print all debug messages - *Default
                      1 - Print on Info -> Error only
                      2 - Print on Debug -> Error only
                      3 - Print on Warning -> Error only
                      4 - Print on Error only
    """
    # initialize colorama
    if not initialized:
        global verbose
        verbose = verbosity
        colorama.init()
        print("PrintHandler initialized")


def sl_print(msg):
    sys.stdout.write(f"\r{msg}")
    sys.stdout.flush()


def write_log(message=None, logfile=None):
    # setup help() return for the function
    """
    function to write messages to a logfile

    :param message: message you want to log
    :param logfile: path to the file you want to act as your logfile
    :return: has no return
    """

    # get the current time as of function call
    now = str(datetime.datetime.now())[:-7]

    # if there is no message skip the nonsense
    if message is None:
        pass
    # if there is a message to write, continue
    else:
        # if the logfile parameter is empty, default to "logfile.txt" otherwise keep parameter entry
        logfile = "logfile.txt" if logfile is None else logfile
        # add a new line to the end of the write if it isn't already present in the content
        content = f"({now})  - {message}\n" if message[-1] != "\n" else f"({now})  - {message}"
        # # set the mode to append if the file already exists or write a new file otherwise
        mode = "a" if os.path.isfile(logfile) else "w"
        # # write log file
        with open(logfile, mode) as f:
            f.write(content)


# function to act as a custom print feature
def c_print(message=None, sep=None, end=None, file=None, flush=False,
            color=None, timestamp=False, log_mode=None, silent=False):
    # setup help() return for the function
    """
    function to act as a custom print feature

    :param message: the string that you want to push to console

    :param sep: separator in print()
    :param end: end of string in print()
    :param file: file in print()
    :param flush: flush in print()

    :param color: color setting of print
                  BLACK, RED, L_RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

    :param timestamp: whether or not to print with a timestamp

    :param log_mode: what warning level to print in if any
                     0 - None
                     1 - INFO - CYAN
                     2 - DEBUG - YELLOW
                     3 - WARNING - L_RED
                     4 - ERROR - RED

    :param silent: bool, True, print or False, do not print
    :return: has no return
    """

    # verbosity level of print (log_mode)
    log_modes = (0, 1, 2, 3, 4)
    if log_mode in log_modes:
        if log_mode == 0:
            log_mode = None

        # INFO
        if log_mode == 1:
            color = "CYAN"
            message = f"INFO: {message}"

        # DEBUG
        if log_mode == 2:
            color = "YELLOW"
            message = f"DEBUG: {message}"

        # WARNING
        if log_mode == 3:
            color = "L_RED"
            message = f"WARNING: {message}"

        # ERROR
        if log_mode == 4:
            color = "RED"
            message = f"ERROR: {message}"

    # if our log_mode is out of range, just set it to None
    else:
        log_mode = None

    # if our timestamp is set to True add a datetime.datetime.now stamp to our message
    if timestamp:
        # datetime.datetime.now() is not subscriptable, so we'll convert it into a string
        # to where we can slice it with indexing to erase the unwanted tail at the end
        now = str(datetime.datetime.now())
        message = f"({now[:-7]}) - {message}"

    # do not print log statements lower than the settings.py allows and the log_mode is acceptable
    do_not_print = True if log_mode in log_modes and verbose > log_mode else False

    # check if we need to skip the print and pass out of the function
    if do_not_print:
        pass

    # otherwise we continue
    else:
        # list of acceptable colors
        colors = ("BLACK", "RED", "L_RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE")
        # if the color isn't in the list of colors or is otherwise empty
        if color is None or color not in colors:
            # make sure we print a freshly reset message as to remove any previous formatting from
            # previous calls
            if colorama is None and not silent:
                print(f"{message}",
                      sep=sep, end=end, file=file, flush=flush)
            elif colorama and not silent:
                if not silent:
                    print(f"{colorama.Fore.RESET}{message}",
                          sep=sep, end=end, file=file, flush=flush)

        # if our log_mode is None or it is acceptable, we assign colors to the message
        if log_mode is None or log_mode in log_modes:
            # write log_mode messages to a log file
            if log_mode in log_modes and log_mode is not None:
                if log_mode >= verbose:
                    write_log(message)

            if colorama is None:
                if not silent:
                    print(f"{message}",
                          sep=sep, end=end, file=file, flush=flush)
            else:
                if not silent:
                    # add color to and print the message, and close
                    # with a Fore.RESET to prevent color settings from bleeding
                    # into subsequently printed statements
                    if color == "BLACK":
                        print(f"{colorama.Fore.WHITE}{message}{colorama.Fore.RESET}",
                              sep=sep, end=end, file=file, flush=flush)
                    if color == "L_RED":
                        print(f"{colorama.Fore.LIGHTRED_EX}{message}{colorama.Fore.RESET}",
                              sep=sep, end=end, file=file, flush=flush)
                    if color == "RED":
                        print(f"{colorama.Fore.RED}{message}{colorama.Fore.RESET}",
                              sep=sep, end=end, file=file, flush=flush)
                    if color == "GREEN":
                        print(f"{colorama.Fore.GREEN}{message}{colorama.Fore.RESET}",
                              sep=sep, end=end, file=file, flush=flush)
                    if color == "YELLOW":
                        print(f"{colorama.Fore.YELLOW}{message}{colorama.Fore.RESET}",
                              sep=sep, end=end, file=file, flush=flush)
                    if color == "BLUE":
                        print(f"{colorama.Fore.BLUE}{message}{colorama.Fore.RESET}",
                              sep=sep, end=end, file=file, flush=flush)
                    if color == "MAGENTA":
                        print(f"{colorama.Fore.MAGENTA}{message}{colorama.Fore.RESET}",
                              sep=sep, end=end, file=file, flush=flush)
                    if color == "CYAN":
                        print(f"{colorama.Fore.CYAN}{message}{colorama.Fore.RESET}",
                              sep=sep, end=end, file=file, flush=flush)
                    if color == "WHITE":
                        print(f"{colorama.Fore.BLACK}{message}{colorama.Fore.RESET}",
                              sep=sep, end=end, file=file, flush=flush)

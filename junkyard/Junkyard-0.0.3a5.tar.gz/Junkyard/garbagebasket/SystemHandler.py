from junkyard.garbagebasket.PrintHandler import c_print


def collapse_list(lst, silent=False):
    """
    function collapses lists into flat strings
    example: collapse_list(['a', 'b', ' ', 'c'])
    input: ['a', 'B', ' ', 'c']
    output: aBc

    :param lst: input list to be collapsed into a single string of characters
    :param silent: toggle silence of error reporting
    :return: collapsed-to-string version of the input list
    """
    function_name = ""
    if isinstance(lst, list):
        o_str = str(lst)
        filters = ["[", "]", ",", "'", " "]
        for f in filters:
            o_str = o_str.replace(f, "")
        return o_str
    else:
        c_print(f"{function_name}: INVALID INPUT", color="RED", silent=silent)


def handle_errors(error, log=True, silent=False, msg=None):
    def error_msg(_msg):
        """ sub function to do error printing """
        if log:
            c_print(_msg, log_mode=4, silent=silent)
        else:
            c_print(_msg, color="RED", silent=silent)

    function_name = "alt_handler"
    handled = False
    errors = {"FileNotFound": f"FileNotFoundError({msg})",
              "PermissionError": f"PermissionError({msg})",
              "FileExistsError": f"FileNotFoundError({msg})",
              "OSError": f"OSError({msg})",
              "IndexError": f"IndexError({msg})",
              "ModeError": f"ModeOutOfRangeError({msg})"}
    for kw in errors:
        if error == kw:
            value = errors.get(kw)
            error_msg(value)
            handled = True
            break

    if not handled:
        c_print(f"UNKNOWN ERROR WENT UNHANDLED", color="RED")

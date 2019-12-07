def pituo(fn):
    """
    Modify a funciton to use Go-styled error handling.

    Arguments:
    fn - The function to apply the modified error handling to.
    """
    def wrapper(*args, **kwargs):
        try:
            val = fn(*args, **kwargs)
        except Exception as err:
            return (None, err)
        else:
            return (val, None)
    return wrapper

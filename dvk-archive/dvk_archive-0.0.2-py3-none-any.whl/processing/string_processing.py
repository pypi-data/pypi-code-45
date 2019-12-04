def extend_int(input_int: int = 0, input_length: int = 0) -> str:
    """
    Returns a string representation of a given int with a given length.
    If the lenght of int is to small, adds leading 0s.
    If values are invalid, returns a string of zeros of the specified length.

    Parameters:
        input_int (int): Int value to return as string.
        input_length (int): Lenth of the string to return.

    Returns:
        str: String value of input_int with the length of input_length
    """
    if input_length is None or input_length == 0:
        return "0"
    if input_int is None:
        return extend_int(0, input_length)
    return_str = str(input_int)
    if input_length < len(return_str):
        return extend_int(0, input_length)
    while len(return_str) < input_length:
        return_str = "0" + return_str
    return return_str

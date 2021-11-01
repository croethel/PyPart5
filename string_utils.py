def str_len(str_in: str) -> int:
    result = len(str_in)
    return result
    """
    Given a string parameter, this function should return the length of the parameter.
    """

def first_char(str_in: str) -> str:
    first_letter = str_in[0]
    return first_letter
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """


def last_char(str_in: str) -> str:
    last_letter = str_in[-1]
    return last_letter
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    return sub_str_in in str_in
    """
    This function determines if the substring exists within the string. Returns True or False.
    """


def substring(str_in: str, start: int, stop: int) -> str:
    return str_in[start:stop]
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """

def opposite_case(str_in: str) -> str:
    return str_in.swapcase()
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """

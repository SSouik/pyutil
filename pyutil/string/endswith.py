"""
Author Samuel Souik

License MIT

endswith.py
"""


def endswith(string, target):
    """
    Description
    ----------
    Check to see if the target string is the end of the string.

    Parameters
    ----------
    string : str - string to check end of\n
    target : str - string to search for

    Returns
    ----------
    bool - True if target is the end of string, False otherwise

    Examples
    ----------
    >>> endswith('Sample string', 'ing')
    -> True
    >>> endswith('abcabcabc', 'abcd')
    -> False
    """
    if not isinstance(string, str):
        raise TypeError("param 'string' must be a string")

    if not isinstance(target, str):
        raise TypeError("param 'target' must be a string")

    return string[len(target) * -1 :] == target

"""
Author Samuel Souik

License MIT

repeat.py
"""


def repeat(string, n):
    """
    Description
    ----------
    Repeat a string 'n' number of times.

    Parameters
    ----------
    string : str - string to repeat
    n : int - number of times to repeat

    Returns
    ----------
    str - string consisting of param string repeated 'n' times

    Example
    ----------
    >>> repeat('abc', 3)
    -> 'abcabcabc'
    """
    if not isinstance(string, str):
        raise TypeError("param 'string' must be a string")

    if not isinstance(n, int):
        raise TypeError("param 'n' must be an integer: 0 <= n <= sys.maxsize")

    if n < 0:
        raise ValueError("param 'n' must be in range 0 <= n <= sys.maxsize")

    n_str = ""
    for _ in range(n):
        n_str = n_str + string
    return n_str

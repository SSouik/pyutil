"""
Author Samuel Souik

License MIT

str_count.py
"""


def str_count(string, target, start=0, end=None):
    """
    Description
    ----------
    Count the number of times a target string appears in a string.

    Parameters
    ----------
    string : str - string to iterate\n
    target : str - string to search for\n
    start : int, optional - start index (default is 0)\n
    end : int, optional - end index (default is None = len(string))

    Returns
    ----------
    int - number of times target appears in string

    Examples
    ----------
    >>> s = 'abcabcabc'
    >>> str_count(s, 'a')
    -> 3
    >>> str_count(s, 'a', 2)
    -> 2
    """
    if not isinstance(string, str):
        raise TypeError("param 'string' must be a string")

    if not isinstance(target, str):
        raise TypeError("param 'target' must be a string")

    if target == "" or string == "":
        return 0

    length = len(string)

    if end is None or end > length:
        end = length

    if start < 0 or end < 0 or start > end:
        raise ValueError(
            "params 'start' and 'end' must be greater than or equal to 0",
            "'end' must be greater than or equal to 'start'",
        )

    if start == end:
        return 0

    n_str = string
    str_len = len(target)
    count = 0
    while start < end:
        try:
            stop = start + str_len
            if stop > end:
                raise IndexError("End reached")

            if n_str[start:stop] == target:
                count = count + 1
            start = start + 1
        except IndexError:
            return count
    return count

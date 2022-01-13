"""
Author Samuel Souik

License MIT.

join.py
"""


def join(seq, separator=","):
    """
    Description
    ----------
    Concatenate all values in a sequence into a string separated by the separator value.

    Parameters
    ----------
    seq : (list or tuple) - sequence of values to concatenate\n
    separator : any, optional - value to separate the values in the sequence (default is ',')

    Returns
    ----------
    str - a string of the values concatenated and separated by the separator value

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5]
    >>> join(lst)
    -> '1,2,3,4,5'
    >>> join(lst, '-')
    -> '1-2-3-4-5'
    """
    if not isinstance(seq, (list, tuple)):
        raise TypeError("param 'seq' must be a list or tuple")

    if not isinstance(separator, str):
        raise TypeError("param 'separator' must be a string")

    string = ""
    i = 0
    length = len(seq)
    while i < length:
        if i == length - 1:
            string = string + str(seq[i])
        else:
            string = string + str(seq[i]) + separator
        i = i + 1
    return string

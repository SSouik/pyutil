"""
Author Samuel Souik

License MIT.

contains.py
"""


def contains(seq, value):
    """
    Description
    ----------
    Checks to see if a value is in the sequence or dictionary.

    Parameters
    ----------
    seq : (list or tuple or set or dict or string) - sequence/dictionary to search in\n
    value : any - value to search for

    Returns
    ----------
    bool - True (value found), False (value not found)

    Examples
    ----------
    >>> lst = [1, 2, 3, 4, 5]
    >>> contains(lst, 4)
    -> True
    >>> contains(lst, 10)
    -> False
    """
    if isinstance(seq, dict):
        return value in seq.keys() or value in seq.values()
    return value in seq

"""
Author Samuel Souik

License MIT.

tail.py
"""

from itertools import islice


def tail(seq):
    """
    Description
    ----------
    Return all values in the sequence except the first.

    Parameters
    ----------
    seq : (list or tuple) - sequence of values

    Returns
    ----------
    generator - a generator containing all values of the sequence but the first

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5, 6]
    >>> tail(lst)
    -> [2, 3, 4, 5, 6] <generator>
    """
    if not isinstance(seq, (list, tuple)):
        raise TypeError("param 'seq' must be a list or tuple")

    return islice(seq, 1, len(seq))

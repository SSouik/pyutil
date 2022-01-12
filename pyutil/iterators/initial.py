"""
Author Samuel Souik

License MIT.

initial.py
"""

from itertools import islice


def initial(seq):
    """
    Description
    ----------
    Create a generator of all the values in a sequence except the last.

    Parameters
    ----------
    seq : (list or tuple or set or string) - sequence to take values from

    Returns
    ----------
    generator - a generator containing all values of the sequence but the last

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5]
    >>> initial(lst)
    -> [1, 2, 3, 4] <generator>
    """
    if not isinstance(seq, (list, tuple, set, str)):
        raise TypeError("param 'seq' must be a list, tuple, set, or string")

    end = len(seq)

    if end > 0:
        end = end - 1

    return islice(seq, 0, end)

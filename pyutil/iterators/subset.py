"""
Author Samuel Souik

License MIT.

subset.py
"""

from itertools import islice


def subset(seq, start=0, end=None):
    """
    Description
    ----------
    Create a subset of the sequence.

    Parameters
    ----------
    seq : (list or tuple) - sequence of values to subset\n
    start : int, optional - start index (default is 0)\n
    end : int, optional - end index (not included) (default is None = len(seq))

    Returns
    ----------
    generator - generator of the subset of values

    Examples
    ----------
    >>> lst = [1, 2, 3, 4, 5, 6, 7]
    >>> subset(lst, 2)
    -> [3, 4, 5, 6, 7] <generator>
    >>> subset(lst, 3, 5)
    -> [4, 5] <generator>
    """
    if not isinstance(seq, (list, tuple)):
        raise TypeError("param 'seq' must be a list or tuple")

    if end is None:
        end = len(seq)

    if start < 0 or end < 0 or start > end:
        raise ValueError(
            "params 'start' and 'end' must be greater than or equal to 0",
            "'end' must be greater than or equal to 'start'",
        )

    return islice(seq, start, end)

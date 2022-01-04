"""
Author Samuel Souik

License MIT.

difference.py
"""

from .contains import contains


def difference(seq, *exclude_seqs):
    """
    Description
    ----------
    Create a generator with all the values in the sequence that are unique.

    Parameters
    ----------
    seq : (list or tuple or set) - sequence to iterate over\n
    *exclude_seqs : (list or tuple or set) - sequences of values to exclude

    Returns
    ----------
    generator - a generator with all unique values

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5]
    >>> difference(lst, [1, 2], [5, 6, 7])
    -> [3, 4] <generator>
    """

    if not isinstance(seq, (list, tuple, set)):
        raise TypeError("param 'seq' must be a list, tuple, or set")

    for item in seq:
        exclude = False
        for exclude_vals in exclude_seqs:
            if contains(exclude_vals, item):
                exclude = True
                break
        if not exclude:
            yield item

"""
Author Samuel Souik

License MIT.

intersection.py
"""

from itertools import islice


def intersection(*seqs):
    """
    Description
    ----------
    Creates a generator containing values found in all sequences.

    Parameters
    ----------
    *seqs : (list or tuple) - sequences to pull common values from

    Returns
    ----------
    generator - a generator containing values found in all sequences

    Example
    ----------
    >>> intersection([1, 2, 3, 4], [3, 4, 5], [2, 3, 4, 5])
    -> [3, 4] <generator>
    """
    for seq in seqs:
        if not isinstance(seq, (list, tuple)):
            raise TypeError("param 'seqs' must contain only lists, tuples, or sets")

    if len(seqs) <= 1:
        return

    def helper(seqs, value):
        for seq in seqs:
            if not value in seq:
                return False
        return True

    for value in seqs[0]:
        if helper(islice(seqs, 1, len(seqs)), value):
            yield value

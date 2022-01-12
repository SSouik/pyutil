"""
Author Samuel Souik

License MIT.

head.py
"""


def head(seq):
    """
    Description
    ----------
    Return the first value in the sequence.

    Parameters
    ----------
    seq : (list or tuple or string) - sequence to get first value of

    Returns
    ----------
    any - first value of the sequence

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5]
    >>> head(lst)
    -> 1
    """
    if len(seq) == 0:
        return None

    return seq[0]

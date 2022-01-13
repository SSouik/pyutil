"""
Author Samuel Souik

License MIT.

last.py
"""


def last(seq):
    """
    Description
    ----------
    Return the last value in the sequence.

    Parameters
    ----------
    seq : (list or tuple or string) - sequence to return last value of

    Returns
    ----------
    any - the last value in the sequence

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5]
    >>> last(lst)
    -> 5
    """
    if not isinstance(seq, (list, tuple, str)):
        raise TypeError("param 'seq' must be a list, tuple, or string")

    if len(seq) == 0:
        return None
    return seq[-1]

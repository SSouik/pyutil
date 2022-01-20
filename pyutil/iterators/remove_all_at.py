"""
Author Samuel Souik

License MIT.

remove_all_at.py
"""


def remove_all_at(seq, remove_indices):
    """
    Description
    ----------
    Remove values at specified indices from the sequence.

    Parameters
    ----------
    seq : (list or tuple) - sequence to remove values from\n
    remove_indices : (list or tuple or set) - sequence of indices to remove

    Returns
    ----------
    generator - a generator containing all values not removed from the sequence

    Example
    ----------
    >>> tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    >>> remove_all_at(tup, [0, 3, 1, 5])
    >>> ['c', 'e', 'g'] <generator>
    """
    if not isinstance(seq, (list, tuple)):
        raise TypeError("param 'seq' must be a list or tuple")

    if not isinstance(remove_indices, (list, tuple, set)):
        raise TypeError("param 'remove_indices' must be a list, tuple, or set")

    for index in remove_indices:
        if not isinstance(index, int) or index < 0:
            raise ValueError(
                "param 'remove_indices' must contain only positive integers"
            )

    index = 0
    while index < len(seq):
        if not index in remove_indices:
            yield seq[index]
        index = index + 1

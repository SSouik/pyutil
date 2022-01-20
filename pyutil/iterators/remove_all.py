"""
Author Samuel Souik

License MIT.

remove_all.py
"""


def remove_all(seq, remove_vals):
    """
    Description
    ----------
    Remove values from the sequence.

    Parameters
    ----------
    seq : (list or tuple) - sequence to remove values from\n
    remove_vals : (list or tuple or set) - sequence of values to remove

    Returns
    ----------
    generator - generator containing all values not removed from the sequence

    Example
    ----------
    >>> remove([1, 2, 3, 4], [2, 1])
    -> [3, 4] <generator>
    """
    if not isinstance(seq, (list, tuple)):
        raise TypeError("param 'seq' must be a list or tuple")

    if not isinstance(remove_vals, (list, tuple, set)):
        raise TypeError("param 'pull_vals' must be a list, tuple, or set")

    for item in seq:
        if not item in remove_vals:
            yield item

"""
Author Samuel Souik

License MIT.

merge.py
"""


def merge(*seqs):
    """
    Description
    ----------
    Create a generator that contains one instance of all values from the sequences.

    Parameters
    ----------
    *seqs : (list or tuple or set or string) - sequences to merge

    Returns
    ----------
    generator - generator containing values from the sequences

    Example
    ----------
    >>> merge([1, 2, 3, 4, 5, 5], (1, 2, 3, 5, 6, 7), {'a', 'b', 'c'})
    -> [1, 2, 3, 4, 5, 6, 7, 'a', 'c', 'b'] <generator>
    """
    for seq in seqs:
        if not isinstance(seq, (list, tuple, set, str)):
            raise TypeError(
                "param 'seqs' must only contain lists, tuples, sets, or strings"
            )

    lst = []
    append = lst.append

    for seq in seqs:
        for item in seq:
            if not item in lst:
                append(item)
                yield item

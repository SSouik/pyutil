"""
Author Samuel Souik

License MIT.

fill.py
"""
from itertools import islice
from .concat import concat


def fill(seq, value, start=0, end=None):
    """
    Description
    ----------
    Fill the sequence with a value.

    Parameters
    ----------
    seq : (list or tuple or set or string) - sequence to fill\n
    value : any - value to fill the sequence with\n
    start : int, optional - starting index (default is 0)\n
    end : int, optional - ending index (not included) (default vlaue is None = len(seq))
    Returns
    ----------
    generator - a generator with the sequence filled

    Examples
    ----------
    >>> lst = [1, 2, 3, 4, 5]
    >>> fill(lst, '*')
    -> ['*', '*', '*', '*', '*'] <generator>
    >>> fill(lst, -1, 1, 3)
    -> [1, -1, -1, 4, 5]
    """
    if not isinstance(seq, (list, tuple, set, str)):
        raise TypeError("param 'seq' must be a list, tuple, set, or string")

    if not isinstance(start, int):
        raise TypeError("params 'start' must be an integer")

    if end is None:
        end = len(seq)

    if not isinstance(end, int):
        raise TypeError("param 'end' must be an integer")

    if start < 0 or end < 0 or start > end:
        raise ValueError(
            "params 'start' and 'end' must be greater than or equal to 0",
            "'start' must be greater than or equal to 'end'",
        )

    lst1 = islice(seq, 0, start)
    lst3 = islice(seq, end, len(seq))

    lst2 = []
    append = lst2.append
    while start < end:
        append(value)
        start = start + 1
    return concat(lst1, lst2, lst3)

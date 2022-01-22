"""
Author Samuel Souik

License MIT.

find_all.py
"""

from itertools import islice


def find_all(seq, func, start=0, end=None):
    """
    Description
    ----------
    Find all the values in the sequence that satisfy the predicate function.

    Parameters
    ----------
    seq : (list or tuple) - sequence to interate\n
    func : callable - predicate function to apply each iteration\n
    start : int, optional - start index (default is 0)\n
    end : int, optional - end index (not included) (default is None = len(seq))

    Returns
    ----------
    python 2:\n
    list - a list of all values that satisfy the predicate function\n

    python 3:\n
    generator - a generator of all values that satisfy the predicate function

    Examples
    ----------
    python 2:
    >>> lst = [1, 2, 3, 4, 5]
    >>> find_all(lst, lambda x: x % 2 == 0)
    -> [2, 4]
    >>> find_all(lst, lambda x: x % 2 == 0, 2)
    -> [4]

    python 3:
    >>> lst = [1, 2, 3, 4, 5]
    >>> find_all(lst, lambda x: x % 2 == 0)
    -> [2, 4] <generator>
    >>> find_all(lst, lambda x: x % 2 == 0, 2)
    -> [4] <generator>
    """
    if not isinstance(seq, (list, tuple)):
        raise TypeError("param 'seq' must be a list or tuple")

    if not callable(func):
        raise TypeError("param 'func' must be a callable")

    if end is None:
        end = len(seq)

    if start < 0 or end < 0 or start > end:
        raise ValueError(
            "params 'start' and 'end' must be greater than or equal to 0",
            "'end' must be greater than or equal to 'start'",
        )

    return filter(func, islice(seq, start, end))

"""
Author Samuel Souik

License MIT.

drop.py
"""

from itertools import islice


def drop(lst, n=1):
    """
    Description
    ----------
    Drop 'n' number of values in the list starting at the beginning.\n
    Mutates the list.

    Parameters
    ----------
    lst : list - list to drop values from\n
    n : int, optional - number of values to drop (default is 1)

    Returns
    ----------
    None

    Examples
    ----------
    >>> lst = [1, 2, 3, 4, 5, 6, 7]
    >>> drop(lst)
    >>> lst
    -> [2, 3, 4, 5, 6, 7]
    >>> lst = [1, 2, 3, 4, 5, 6, 7]
    >>> drop(lst, 4)
    >>> lst
    -> [5, 6, 7]
    """
    lst[:] = list(islice(lst, n, len(lst)))

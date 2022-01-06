"""
Author Samuel Souik

License MIT.

drop_while.py
"""

from itertools import islice


def drop_while(lst, func):
    """
    Description
    ----------
    Drop values from the list as long as the predicate function is satisfied.\n
    Starts at the beginning of the list.\n
    Mutates the list.

    Parameters
    ----------
    lst : list - list to drop values from\n
    func : callable - predicate function to apply each iteratrion

    Returns
    ----------
    None

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5, 6]
    >>> drop_while(lst, lambda x: x != 3)
    >>> lst
    -> [3, 4, 5, 6]
    """
    if not isinstance(lst, list):
        raise TypeError("param 'lst' must be a list")

    if not callable(func):
        raise TypeError("param 'func' must be a callable")

    n = 0
    for item in lst:
        if func(item):
            n = n + 1
        else:
            break
    lst[:] = list(islice(lst, n, len(lst)))

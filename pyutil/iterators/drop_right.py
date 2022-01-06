"""
Author Samuel Souik

License MIT.

drop.py
"""

from itertools import islice


def drop_right(lst, n=1):
    """
    Description
    ----------
    Drop 'n' number of values in the list starting at the end.\n
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
    >>> drop_right(lst)
    >>> lst
    -> [1, 2, 3, 4, 5, 6]
    >>> lst = [1, 2, 3, 4, 5, 6, 7]
    >>> drop_right(lst, 4)
    >>> lst
    -> [1, 2, 3]
    """
    if not isinstance(lst, list):
        raise TypeError("param 'lst must be a list")

    length = len(lst)

    if n > length:
        raise ValueError("param 'n' must be greater than the length of 'lst'")

    if n < 0:
        raise ValueError("param 'n' must be greater than or equal to 0")

    lst[:] = list(islice(lst, 0, length - n))

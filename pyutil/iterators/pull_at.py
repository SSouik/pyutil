"""
Author Samuel Souik

License MIT.

pull_at.py
"""


def pull_at(lst, *pull_indices):
    """
    Description
    ----------
    Remove values at all specified indices.\n
    Mutates the list.

    Parameters
    ----------
    lst : list - list to remove values from\n
    *pull_indices : int - indices to remove

    Returns
    ----------
    None

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5, 6, 7]
    >>> pull_at(lst, 0, 2, 4)
    >>> lst
    -> [2, 4, 6, 7]
    """
    if not isinstance(lst, list):
        raise TypeError("param 'lst' must be a list")

    for index in pull_indices:
        if not isinstance(index, int) or index < 0:
            raise ValueError("param 'pull_indices' must contain only positive integers")

    lst_len = len(lst)
    offset = 0
    i = 0

    for index in pull_indices:
        if index <= lst_len - 1:
            del lst[index - offset]
            try:
                if index < pull_indices[i + 1]:
                    offset = offset + 1
            except IndexError:
                pass
            i = i + 1

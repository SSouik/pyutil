"""
Author Samuel Souik

License MIT.

pull_all.py
"""


def pull_all(lst, pull_vals):
    """
    Description
    ----------
    Remove values from the list.\n
    Mutates the list.

    Parameters
    ----------
    lst : list - list to remove values from\n
    pull_vals : (list or tuple or set) - sequence of values to remove

    Returns
    ----------
    None

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 2, 4, 5, 6, 1]
    >>> pull(lst, [2, 4, 1])
    >>> lst
    -> [3, 5, 6]
    """
    if not isinstance(lst, list):
        raise TypeError("param 'lst' must be a list")

    if not isinstance(pull_vals, (list, tuple, set)):
        raise TypeError("param 'pull_vals' must be a list, tuple, or set")

    remove = lst.remove

    for value in pull_vals:
        while value in lst:
            remove(value)

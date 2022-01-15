"""
Author Samuel Souik

License MIT.

pull.py
"""


def pull(lst, *pull_vals):
    """
    Description
    ----------
    Remove values from the list.\n
    Mutates the list.

    Parameters
    ----------
    lst : list - list to remove values from\n
    *pull_vals : any - values to remove

    Returns
    ----------
    None

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 2, 4, 5, 6, 1]
    >>> pull(lst, 2, 4, 1)
    >>> lst
    -> [3, 5, 6]
    """
    if not isinstance(lst, list):
        raise TypeError("param 'lst' must be a list")

    remove = lst.remove

    for value in pull_vals:
        while value in lst:
            remove(value)

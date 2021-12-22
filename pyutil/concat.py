"""
Author Samuel Souik

License MIT.

concat.py
"""


def concat(*values):
    """
    Description
    ----------
    Creates a generator concatenating all the lists and/or values.

    Parameters
    ----------
    *values : any - values to concatenate into one list

    Returns
    ----------
    generator - generator containing all the values passed as parameters

    Examples
    ----------
    >>> lst = [1, 2, 3]
    >>> concat(lst, [4, 5], 'a', ['b', 'c'], 123, [[5]])
    -> [1, 2, 3, 4, 5, 'a', 'b', 'c', 123, [5]] <generator>
    """
    for val in values:
        try:
            for item in val:
                yield item
        except TypeError:
            yield val

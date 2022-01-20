"""
Author Samuel Souik

License MIT.

entries.py
"""


def entries(dct):
    """
    Description
    ----------
    Creates a generator of all key value pairs in the dictionary.

    Parameters
    ----------
    dct : dict - dictionary to get key value pairs from

    Returns
    ----------
    generator - generator containing all key value pairs

    Example
    ----------
    >>> entries({'a': 1, 'b': 2})
    -> [('a', 1), ('b', 2)] <generator>
    """
    if not isinstance(dct, dict):
        raise TypeError("param 'dct' must be a dict")

    for key in dct:
        yield (key, dct[key])

"""
Author Samuel Souik

License MIT.

assign.py
"""


def assign(target, *sources):
    """
    Description
    ----------
    Assign all values from the sources into the target dictioanary.\n
    Mutates target dictionary.

    Parameters
    ----------
    target : dict - target dictionary to assign values to\n
    *sources : dict - dictionaries to pull keys and vlaues from

    Returns
    ----------
    dict - dictionary containing keys and values from target and *sources

    Example
    ----------
    >>> assign({}, {'a': 1, 'b': 2})
    -> {'a': 1, 'b': 2}
    """
    if not isinstance(target, dict):
        raise TypeError("param 'target' must be a dict")

    for source in sources:
        if not isinstance(source, dict):
            raise TypeError("param 'target' must be a dict")

    for dct in sources:
        for key in dct:
            target[key] = dct[key]
    return target

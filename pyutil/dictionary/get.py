"""
Author Samuel Souik

License MIT

get.py
"""


def get(dct, key_path, default=None):
    """
    Description
    ----------
    Get the value at the specified key path. If the path does not exist
    then the default value wll be returned.

    Parameters
    ----------
    dct : dict - dictionary to get key value pairs from\n
    key_path : string - path to the key as a string\n
    default: any, optional - default value to be returned,
    if the key does not exist or is None (default is None)

    Returns
    ----------
    any - the value at the key path or the deafult value if not found

    Example
    ----------
    >>> get({'a': 1, 'b': 2}, 'a')
    -> 1
    """

    if not isinstance(dct, dict):
        raise TypeError("param 'dct' must be a dictionary")

    if not isinstance(key_path, str):
        raise TypeError("param 'key_path' must be a string")

    keys = key_path.split(".")
    value = dct

    for key in keys:
        try:
            value = value.get(key, default)
        except AttributeError:
            return default

    return value

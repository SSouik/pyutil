"""
Author Samuel Souik

License MIT.

countby.py
"""


def countby(seq, key):
    """
    Description
    ----------
    Create a dictionary with keys composed of the return value of the funcion/key\n
    applied to each item in the sequence. The value for each key is the number of times\n
    each key was returned.

    Parameters
    ----------
    seq : (list or tuple or set) - sequence to iterate\n
    key : (callable or dictionary key) - callable to apply each iteration or key to extract\n
    from each dictionary per iteration

    Returns
    ----------
    dict : a dictionary containing keys returned from each iteration
    and the number of times it was returned

    Examples
    ----------
    >>> def even_odd(x):
    ...   if x % 2 == 0:
    ...     return 'even'
    ...   return 'odd'

    >>> lst = [1, 2, 3, 4, 5, 6, 7]
    >>> countby(lst, even_odd)
    -> {'even': 3, 'odd': 4}

    >>> people = [
    ... {'name': 'Sam' 'gender': 'male'},
    ... {'name': 'John' 'gender': 'male'},
    ... {'name': 'Jane' 'gender': 'female'},
    ... {'name': 'Chase' 'gender': 'male'},
    ... {'name': 'Melanie' 'gender': 'female'}]
    >>> countby(people, 'gender')
    -> {'male': 3, 'female': 2}
    """
    if not isinstance(seq, (list, tuple, set)):
        raise TypeError("param 'seq' must be a list, tuple, or set")

    dct = {}
    get = dct.get
    if callable(key):
        for item in seq:
            val = key(item)
            if get(val) is not None:
                dct[val] = dct[val] + 1
            else:
                dct[val] = 1
    else:
        for item in seq:
            val = item[key]
            if get(val) is not None:
                dct[val] = dct[val] + 1
            else:
                dct[val] = 1
    return dct

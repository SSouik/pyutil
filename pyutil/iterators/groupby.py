"""
Author Samuel Souik

License MIT.

groupby.py
"""


def groupby(seq, key):
    """
    Description
    ----------
    Create a dictionary with keys composed of the return value of the funcion/key\n
    applied to each item in the sequence. The value for each key is a list of values\n
    that produced the key.

    Parameters
    ----------
    seq : (list or tuple or set) - sequence to iterate\n
    key : (callable or dictionary key) - callable to apply each iteration or key to extract\n
    from each dictionary per iteration

    Returns
    ----------
    dict : a dictionary containing keys returned from each iteration and the values that returned it

    Examples
    ----------
    >>> def even_odd(x):
    ...   if x % 2 == 0:
    ...     return 'even'
    ...   return 'odd'

    >>> lst = [1, 2, 3, 4, 5, 6, 7]
    >>> groupby(lst, even_odd)
    -> {'even': [2, 4, 6], 'odd': [1, 3, 5, 7]}

    >>> people = [
    ... {'name': 'Sam', 'gender': 'male'},
    ... {'name': 'John', 'gender': 'male'},
    ... {'name': 'Jane', 'gender': 'female'},
    ... {'name': 'Chase', 'gender': 'male'},
    ... {'name': 'Melanie', 'gender': 'female'}]
    >>> groupby(people, 'gender')
    -> {
        'male': [
          {'name': 'Sam', 'gender': 'male'},
          {'name': 'John', 'gender': 'male'},
          {'name': 'Chase', 'gender': 'male'}
        ],
        'female': [
          {'name': 'Jane', 'gender': 'female'},
          {'name': 'Melanie', 'gender': 'female'}
        ]
       }
    """
    if not isinstance(seq, (list, tuple, set)):
        raise TypeError("param 'seq' must be a list, tuple, or set")

    if len(seq) == 0:
        return {}

    dct = {}
    get = dct.get
    if callable(key):
        for item in seq:
            val = key(item)
            if get(val) is not None:
                dct[val].append(item)
            else:
                dct[val] = [item]
    else:
        for item in seq:
            val = item[key]
            if get(val) is not None:
                dct[val].append(item)
            else:
                dct[val] = [item]
    return dct

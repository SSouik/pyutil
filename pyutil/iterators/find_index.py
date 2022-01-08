"""
Author Samuel Souik

License MIT.

find_index.py
"""


def find_index(seq, func, from_index=0):
    """
    Description
    ----------
    Find the index of the first value that satisfies the predicate function.\n
    Returns -1 if no value was found.

    Parameters
    ----------
    seq : (list or tuple) - sequence to iterate\n
    func : callable - predicate function to apply each iteration\n
    from_index : int, optional - start index (default is 0)

    Returns
    ----------
    int : index of the value found or -1 if no value satisfied the predicate function

    Example
    ----------
    >>> lst = ['abc' ,'bcde', 'cdefg', 'defghi']
    >>> find_index(lst, lambda x: len(x) == 4)
    -> 1
    >>> find_index(lst, lambda x: len(x) == 4, 2)
    -> -1
    >>> find_index(lst, lambda x: len(x) == 5, -1)
    -> 2
    """
    if not isinstance(seq, (list, tuple)):
        raise TypeError("param 'seq' must be a list or tuple")

    if not callable(func):
        raise TypeError("param 'func' must be a callable")

    if not isinstance(from_index, int):
        raise TypeError("param 'from_index' must be an integer")

    if from_index < 0:
        length = len(seq) * -1
        while from_index >= length:
            if func(seq[from_index]):
                return (length * -1) + from_index
            from_index = from_index - 1
        return -1

    while from_index < len(seq):
        if func(seq[from_index]):
            return from_index
        from_index = from_index + 1
    return -1

"""
Author Samuel Souik

License MIT.

some.py
"""


def some(seq, func):
    """
    Description
    ----------
    Return True if some value in the sequence satisfies the predicate function.\n
    Returns False otherwise.

    Parameters
    ----------
    seq : (list or tuple or set or dict) - sequence to iterate\n
    func : callable - predicate function to apply each iteration

    Returns
    ----------
    bool - True if some value satisfies the predicate function, False otherwise

    Example
    ----------
    >>> lst = ['', 0, None, 1000]
    >>> some(lst, bool)
    -> True
    """
    if not isinstance(seq, (list, tuple, set)):
        raise TypeError("param 'seq' must be a list, tuple, or set")

    if not callable(func):
        raise TypeError("param 'func' must be a callable")

    for item in seq:
        if func(item):
            return True
    return False

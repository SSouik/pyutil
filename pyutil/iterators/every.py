"""
Author Samuel Souik

License MIT.

every.py
"""


def every(seq, func):
    """
    Description
    ----------
    Apply callable on each value in the sequence and return True if\n
    all values satisfy the predicate function. Return False otherwise.

    Parameters
    ----------
    seq : (list or tuple or set or dict or string) - sequence to iterate\n
    func : callable - predicate function to apply each iteration

    Returns
    ----------
    bool - True if all values satisfy the predicate function, False otherwise

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5, 6, 7]
    >>> every(lst, lambda x: x % 2 == 0)
    -> False
    """
    if not isinstance(seq, (list, tuple, set, dict, str)):
        raise TypeError("param 'seq' must be a list, tuple, set, dict, or string")

    if not callable(func):
        raise TypeError("param 'func' must be a callable")

    if len(seq) == 0:
        return False

    for item in seq:
        if not func(item):
            return False
    return True

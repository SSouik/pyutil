"""
Author Samuel Souik

License MIT.

find.py
"""

from itertools import islice


def find(seq, func, start=0, end=None):
    """
    Description
    ----------
    Find and return the first value in the sequence that satisfies the predicate function.

    Parameters
    ----------
    seq : (list or tuple or set) - sequence to iterate\n
    func : callable - predicate function to apply each iteration\n
    start : int, optional - start index (default is 0)\n
    end : int, optional - end index (not included) (default is None = len(seq))

    Returns
    ----------
    any - the first value that satisfies the predicate function or None

    Examples
    ----------
    >>> people = [
    ... {'name': 'Sam' 'age': 22},
    ... {'name': 'Liam', 'age': 0},
    ... {'name': 'Wes', 'age': 32}]
    >>> find(people, lambda person: person['age'] == 0)
    -> {'name': 'Liam', 'age': 0}
    >>> find(people, lambda person: person['age'] == 32, 1)
    -> {'name': 'Wes', 'age': 32}
    """
    if not isinstance(seq, (list, tuple)):
        raise TypeError("param 'seq' must be a list or tuple")

    if not callable(func):
        raise TypeError("param 'func' must be a callable")

    if end is None:
        end = len(seq)

    if start < 0 or end < 0 or start > end:
        raise ValueError(
            "params 'start' and 'end' must be greater than or equal to 0",
            "'end' must be greater than or equal to 'start'",
        )

    for item in islice(seq, start, end):
        if func(item):
            return item
    return None

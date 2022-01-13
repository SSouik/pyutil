"""
Author Samuel Souik

License MIT.

pipe.py
"""


def pipe(data, *funcs):
    """
    Description
    ----------
    Pipe data through a series of functions.

    Parameters
    ----------
    data : any - data to pipe\n
    *funcs : callable - functions for data to be piped through

    Returns
    ----------
    any - result of data being passed through all the functions

    Example
    ----------
    >>> def increment(x):
    ...   return x + 1
    ...
    >>> def double(x):
    ...   return x * 2
    ...
    >>> pipe(10, increment, double, str)
    -> '22'
    """
    for func in funcs:
        if not callable(func):
            raise TypeError("param 'funcs' must only be functions")

    value = data
    for func in funcs:
        value = func(value)
    return value

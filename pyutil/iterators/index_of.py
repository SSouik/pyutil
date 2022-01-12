"""
Author Samuel Souik

License MIT.

index_of.py
"""


def index_of(seq, value, from_index=0):
    """
    Description
    ----------
    Return the index of a value in a sequence.\n
    Returns -1 if the value was not found.

    Parameters
    ----------
    seq : (list or tuple or string) - sequence to iterate\n
    value: any - value to search for\n
    from_index : int, optional - start index (default is 0)

    Returns
    ----------
    int - index of value or -1 if the value was not found

    Example
    ----------
    >>> lst = [1, 2, 3, 4, 5]
    >>> index_of(lst, 3)
    -> 2
    >>> index_of(lst, 3, 3)
    -> -1
    """
    if not isinstance(seq, (list, tuple, str)):
        raise TypeError("param 'seq' must be a list, tuple, or string")

    if from_index < 0:
        length = len(seq) * -1
        while from_index >= length:
            if seq[from_index] == value:
                return (length * -1) + from_index
            from_index = from_index - 1
        return -1

    while from_index < len(seq):
        if seq[from_index] == value:
            return from_index
        from_index = from_index + 1
    return -1

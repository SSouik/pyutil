"""
Author Samuel Souik

License MIT

replace.py
"""


def replace(string, target, replacement, n=None):
    """
    Description
    ----------
    Replace a target string with a replacement string 'n' number of times.

    Parameters
    ----------
    string : str - string to iterate\n
    target : str - string to search for\n
    replacement : str - string to replace target with\n
    n : int, optional - number of times to replace target string

    Returns
    ----------
    str - string with target replaced by replacement 'n' number of times

    Examples
    ----------
    >>> replace('abcsabcsabcsefgs', 'abc', 'x')
    -> 'xsxsxsefgs'
    >>> replace('abcsabcsabcsefgs', 'abc', 'x', 2)
    -> 'xsxsabcsefgs'
    """
    if not isinstance(string, str):
        raise TypeError("param 'string' must be a string")

    if not isinstance(target, str):
        raise TypeError("param 'target' must be a string")

    if not isinstance(replacement, str):
        raise TypeError("param 'replacement' must be a string")

    if n is not None:
        if not isinstance(n, int):
            raise TypeError("param 'n' must be an integer")

        if n < 0:
            raise ValueError("param 'n' must be in range 0 <= n <= sys.maxsize")

    temp_str = string.strip()
    n_str = ""
    str_len = len(target)
    i = 0
    count = 0

    if str_len == 0:
        return string

    if n is None:
        count = None

    if count is None:
        while True:
            try:
                stop = i + str_len
                if stop > len(temp_str):
                    raise IndexError("Stop greater than length of string")

                if temp_str[i:stop] == target:
                    n_str = n_str + replacement
                    i = stop
                else:
                    n_str = n_str + temp_str[i]
                    i = i + 1
            except:
                return n_str + temp_str[i::]

    while count < n:
        try:
            stop = i + str_len
            if stop > len(temp_str):
                raise IndexError("Stop greater than length of string")

            if temp_str[i:stop] == target:
                n_str = n_str + replacement
                i = stop
                count = count + 1
            else:
                n_str = n_str + temp_str[i]
                i = i + 1
        except:
            return n_str + temp_str[i::]
    return n_str + temp_str[i::]

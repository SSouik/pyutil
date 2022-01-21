"""
  Author Samuel Souik.

  License MIT.
  
  This module provides a functional library for Python.
  Functional methods provided operate on lists, tuples, sets, dictionaries, and strings.
  The module was inspired by the JavaScript library lodash and Python
  modules itertools and toolz.
"""

########################################################
#                                                      #
# The following functions operate on Python sequences. #
# (lists, tuples, sets, dictionaries and strings)      #
#                                                      #
########################################################


def str_remove(string, target, start=0, end=None):
    """
    Description
    ----------
    Remove a target string from the string.

    Parameters
    ----------
    string : str - string to iterate\n
    target : str - string to remove\n
    start : int, optional - start index (default is 0)\n
    end : int, optional - end index (default is None = len(string))

    Returns
    ----------
    str - string with target removed

    Examples
    ----------
    >>> str_remove('abcabcabcxyz', 'abc')
    -> 'xyz'
    >>> str_remove('abcabcabcxyz', 'abc', 1)
    -> 'abcxyz'
    """
    if end == None:
        end = len(string)

    if start < 0:
        raise ValueError("Start index must be an integer: 0 <= x <= sys.maxsize")

    if end < 0:
        raise ValueError("End index must be an integer: 0 <= x <= sys.maxsize")

    temp_str = string.strip()
    n_str = ""
    str_len = len(target)
    beg_str = temp_str[0:start]
    end_str = temp_str[end + 1 : len(string)]

    if str_len > (end - start):
        return temp_str

    while start < end:
        try:
            stop = start + str_len
            substring = temp_str[start:stop]
            if substring != target:
                n_str = n_str + substring[0]
                start = start + 1
            else:
                start = start + str_len
        except:
            return beg_str + n_str + end_str
    return beg_str + n_str + end_str


def words(string):
    """
    Description
    ----------
    Find all substrings in the string that contain alphabetical characters.

    Parameters
    ----------
    string : str - string to extract words from

    Returns
    ----------
    generator - generator containing strings with aplhabetical characters

    Example
    ----------
    >>> words('Hello there! I want to talk.')
    -> ['Hello', 'there', 'I', 'want', 'to', 'talk'] <generator>
    """
    word = ""
    for char in string:
        if char.isalpha() or char == "'":
            word = word + char
        else:
            if word != "":
                yield word
                word = ""

    if word != "":
        yield word

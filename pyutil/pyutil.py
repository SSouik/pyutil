'''
  Author Samuel Souik.

  License MIT.
  
  This module provides a functional library for Python.
  Functional methods provided operate on lists, tuples, sets, dictionaries, and strings.
  The module was inspired by the JavaScript library lodash and Python
  modules itertools and toolz.
'''

from itertools import islice

########################################################
#                                                      #
# The following functions operate on Python sequences. #
# (lists, tuples, sets, dictionaries and strings)      #
#                                                      #
########################################################

# dictionary methods

def assign(target, *sources):
  '''
  Description
  ----------
  Assign all values from the sources into the target dictioanary.\n
  Mutates target dictionary.

  Parameters
  ----------
  target : dict - target dictionary to assign values to\n
  *sources : dict - dictionaries to pull keys and vlaues from

  Returns
  ----------
  dict - dictionary containing keys and values from target and *sources

  Example
  ----------
  >>> assign({}, {'a': 1, 'b': 2})
  -> {'a': 1, 'b': 2}
  '''
  for dct in sources:
    for key in dct:
      target[key] = dct[key]
  return target

def entries(dct):
  '''
  Description
  ----------
  Creates a generator of all key value pairs in the dictionary.

  Parameters
  ----------
  dct : dict - dictionary to get key value pairs from

  Returns
  ----------
  generator - generator containing all key value pairs

  Example
  ----------
  >>> entries({'a': 1, 'b': 2})
  -> [('a', 1), ('b', 2)] <generator>
  '''
  for key in dct:
    yield (key, dct[key])

# string methods

def str_count(string, target, start = 0, end = None):
  '''
  Description
  ----------
  Count the number of times a target string appears in a string.

  Parameters
  ----------
  string : str - string to iterate\n
  target : str - string to search for\n
  start : int, optional - start index (default is 0)\n
  end : int, optional - end index (default is None = len(string))

  Returns
  ----------
  int - number of times target appears in string

  Examples
  ----------
  >>> s = 'abcabcabc'
  >>> str_count(s, 'a')
  -> 3
  >>> str_count(s, 'a', 2)
  -> 2
  '''
  if end == None:
    end = len(string)
  
  if start < 0:
    raise ValueError('Start index must be an integer: 0 <= x <= sys.maxsize')

  if end < 0:
    raise ValueError('End index must be an integer: 0 <= x <= sys.maxsize')

  if start >= end:
    return 0

  n_str = string
  str_len = len(target)
  count = 0
  while start < end:
    try:
      stop = start + str_len
      if stop > end:
        raise IndexError('End reached')

      if n_str[start:stop] == target:
        count = count + 1
      start = start + 1
    except:
      return count
  return count

def endswith(string, target):
  '''
  Description
  ----------
  Check to see if the target string is the end of the string.

  Parameters
  ----------
  string : str - string to check end of\n
  target : str - string to search for

  Returns
  ----------
  bool - True if target is the end of string, False otherwise

  Examples
  ----------
  >>> endswith('Sample string', 'ing')
  -> True
  >>> endswith('abcabcabc', 'abcd')
  -> False
  '''
  return string[len(target) * -1:] == target

def repeat(string, n):
  '''
  Description
  ----------
  Repeat a string 'n' number of times.

  Parameters
  ----------
  string : str - string to repeat
  n : int - number of times to repeat

  Returns
  ----------
  str - string consisting of param string repeated 'n' times

  Example
  ----------
  >>> repeat('abc', 3)
  -> 'abcabcabc'
  '''
  if not type(n) is int:
    raise TypeError('param \'n\' must be an integer: 0 <= n <= sys.maxsize')

  n_str = ''
  for i in range(n):
    n_str = n_str + string
  return n_str

def replace(string, target, replacement, n = None):
  '''
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
  '''
  if not type(n) is int:
    raise TypeError('param \'n\' must be an integer: 0 <= n <= sys.maxsize')

  if n != None:
    if n < 0:
      raise ValueError('\'n\' must be an integer: 0 <= n <= sys.maxsize')

  temp_str = string.strip()
  n_str = ''
  str_len = len(target)
  i = 0
  count = 0

  if n == None:
    count = None

  if count == None:
    while True:
      try:
        stop = i + str_len
        if stop > len(temp_str):
          raise IndexError('Stop greater than length of string')

        if temp_str[i:stop] == target:
          n_str = n_str + replacement
          i = stop
        else:
          n_str = n_str + temp_str[i]
          i = i + 1
      except:
        return n_str + temp_str[i::]
    return n_str

  while count < n:
    try:
      stop = i + str_len
      if stop > len(temp_str):
        raise IndexError('Stop greater than length of string')

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

def str_remove(string, target, start = 0, end = None):
  '''
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
  '''
  if end == None:
    end = len(string)
  
  if start < 0:
    raise ValueError('Start index must be an integer: 0 <= x <= sys.maxsize')

  if end < 0:
    raise ValueError('End index must be an integer: 0 <= x <= sys.maxsize')
  
  temp_str = string.strip()
  n_str = ''
  str_len = len(target)
  beg_str = temp_str[0:start]
  end_str = temp_str[end+1:len(string)]

  if str_len > (end - start):
    return temp_str
  
  while start < end:
    try:
      stop = start + str_len
      substring = temp_str[start: stop]
      if substring != target:
        n_str = n_str + substring[0]
        start = start + 1
      else:
        start = start + str_len
    except:
      return beg_str + n_str + end_str
  return beg_str + n_str + end_str

def words(string):
  '''
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
  '''
  word = ''
  for char in string:
    if char.isalpha() or char == '\'':
      word = word + char
    else:
      if word != '':
        yield word
        word = ''
  
  if word != '':
    yield word
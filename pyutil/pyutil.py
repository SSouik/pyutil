'''
  Author Samuel Souik.

  License MIT.
  
  This module provides a functional library for Python.
  Functional methods provided operate on lists, tuples, sets, dictionaries, and strings.
  The module was inspired by the JavaScript library lodash and Python
  modules itertools and toolz.
'''

from itertools import islice
from .iterators.concat import concat
from .iterators.contains import contains

########################################################
#                                                      #
# The following functions operate on Python sequences. #
# (lists, tuples, sets, dictionaries and strings)      #
#                                                      #
########################################################

def countby(seq, key):
  '''
  Description
  ----------
  Create a dictionary with keys composed of the return value of the funcion/key\n
  applied to each item in the sequence. The value for each key is the number of times\n
  each key was returned.

  Parameters
  ----------
  seq : (list or tuple or set) - sequence to iterate\n
  key : (callable or dictionary key) - callable to apply each iteration or key to extract\n 
  from each dictionary per iteration

  Returns
  ----------
  dict : a dictionary containing keys returned from each iteration and the number of times it was returned
  
  Examples
  ----------
  >>> def even_odd(x):
  ...   if x % 2 == 0:
  ...     return 'even'
  ...   return 'odd'
  
  >>> lst = [1, 2, 3, 4, 5, 6, 7]
  >>> countby(lst, even_odd)
  -> {'even': 3, 'odd': 4}

  >>> people = [
  ... {'name': 'Sam' 'gender': 'male'},
  ... {'name': 'John' 'gender': 'male'},
  ... {'name': 'Jane' 'gender': 'female'},
  ... {'name': 'Chase' 'gender': 'male'},
  ... {'name': 'Melanie' 'gender': 'female'}]
  >>> countby(people, 'gender')
  -> {'male': 3, 'female': 2}
  '''
  dct = {}
  get = dct.get
  if callable(key):
    for item in seq:
      val = key(item)
      if get(val) != None:
        dct[val] = dct[val] + 1
      else:
        dct[val] = 1
  else:
    for item in seq:
      val = item[key]
      if get(val) != None:
            dct[val] = dct[val] + 1
      else:
        dct[val] = 1
  return dct

def difference(seq, *exclude_seqs):
  '''
  Description
  ----------
  Create a generator with all the values in the sequence that are unique.

  Parameters
  ----------
  seq : (list or tuple or set) - sequence to iterate over\n
  *exclude_seqs : (list or tuple or set) - sequences of values to exclude

  Returns
  ----------
  generator - a generator with all unique values

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5]
  >>> difference(lst, [1, 2], [5, 6, 7])
  -> [3, 4] <generator>
  '''
  for item in seq:
    exclude = False
    for exclude_vals in exclude_seqs:
      if contains(exclude_vals, item):
        exclude = True
        break
    if not exclude:
      yield item
  
def drop(lst, n = 1):
  '''
  Description
  ----------
  Drop 'n' number of values in the list starting at the beginning.\n
  Mutates the list.

  Parameters
  ----------
  lst : list - list to drop values from\n
  n : int, optional - number of values to drop (default is 1)

  Returns
  ----------
  None
  
  Examples
  ----------
  >>> lst = [1, 2, 3, 4, 5, 6, 7]
  >>> drop(lst)
  >>> lst
  -> [2, 3, 4, 5, 6, 7]
  >>> lst = [1, 2, 3, 4, 5, 6, 7]
  >>> drop(lst, 4)
  >>> lst
  -> [5, 6, 7]
  '''
  lst[:] = list(islice(lst, n, len(lst)))
  
def drop_right(lst, n = 1):
  '''
  Description
  ----------
  Drop 'n' number of values in the list starting at the end.\n
  Mutates the list.

  Parameters
  ----------
  lst : list - list to drop values from\n
  n : int, optional - number of values to drop (default is 1)

  Returns
  ----------
  None

  Examples
  ----------
  >>> lst = [1, 2, 3, 4, 5, 6, 7]
  >>> drop_right(lst)
  >>> lst
  -> [1, 2, 3, 4, 5, 6]
  >>> lst = [1, 2, 3, 4, 5, 6, 7]
  >>> drop_right(lst, 4)
  >>> lst
  -> [1, 2, 3]
  '''
  lst[:] = list(islice(lst, 0, len(lst) - n))

def drop_right_while(lst, func):
  '''
  Description
  ----------
  Drop values from the list as long as the predicate function is satisfied.\n
  Starts at the end of the list.\n
  Mutates the list.

  Parameters
  ----------
  lst : list - list to drop values from\n
  func : callable - predicate function to apply each iteratrion

  Returns
  ----------
  None

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5, 6]
  >>> drop_right_while(lst, lambda x: x != 3)
  >>> lst
  -> [1, 2, 3]
  '''
  n = len(lst)
  for item in reversed(lst):
    if func(item):
      n = n - 1
    else:
      break
  lst[:] = list(islice(lst, 0, n))

def drop_while(lst, func):
  '''
  Description
  ----------
  Drop values from the list as long as the predicate function is satisfied.\n
  Starts at the beginning of the list.\n
  Mutates the list.

  Parameters
  ----------
  lst : list - list to drop values from\n
  func : callable - predicate function to apply each iteratrion

  Returns
  ----------
  None

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5, 6]
  >>> drop_while(lst, lambda x: x != 3)
  >>> lst
  -> [3, 4, 5, 6]
  '''
  n = 0
  for item in lst:
    if func(item):
      n = n + 1
    else:
      break
  lst[:] = list(islice(lst, n, len(lst)))

def every(seq, func):
  '''
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
  '''
  for item in seq:
    if not func(item):
      return False
  return True

def fill(seq, value, start = 0, end = None):
  '''
  Description
  ----------
  Fill the sequence with a value.

  Parameters
  ----------
  seq : (list or tuple or set or string) - sequence to fill\n
  value : any - value to fill the sequence with\n
  start : int, optional - starting index (default is 0)\n
  end : int, optional - ending index (not included) (default vlaue is None = len(seq))
  Returns
  ----------
  generator - a generator with the sequence filled

  Examples
  ----------
  >>> lst = [1, 2, 3, 4, 5]
  >>> fill(lst, '*')
  -> ['*', '*', '*', '*', '*'] <generator>
  >>> fill(lst, -1, 1, 3)
  -> [1, -1, -1, 4, 5]
  '''
  if end == None:
    end = len(seq)
  
  lst1 = islice(seq, 0, start)
  lst3 = islice(seq, end, len(seq))

  lst2 = []
  append = lst2.append
  while start < end:
    append(value)
    start = start + 1
  return concat(lst1, lst2, lst3)

def find(seq, func, start = 0, end = None):
  '''
  Description
  ----------
  Find and return the first value in the sequence that satisfies the predicate function.

  Parameters
  ----------
  seq : (list or tuple or set or dict) - sequence to iterate\n
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
  '''
  if end == None:
    end = len(seq)
  
  for item in islice(seq, start, end):
    if func(item):
      return item
  return None

def find_all(seq, func, start = 0, end = None):
  '''
  Description
  ----------
  Find all the values in the sequence that satisfy the predicate function.

  Parameters
  ----------
  seq : (list or tuple or set or dict) - sequence to interate\n
  func : callable - predicate function to apply each iteration\n
  start : int, optional - start index (default is 0)\n
  end : int, optional - end index (not included) (default is None = len(seq))

  Returns
  ----------
  python 2:\n
  list - a list of all values that satisfy the predicate function\n
  
  python 3:\n
  generator - a generator of all values that satisfy the predicate function

  Examples
  ----------
  python 2:
  >>> lst = [1, 2, 3, 4, 5]
  >>> find_all(lst, lambda x: x % 2 == 0)
  -> [2, 4]
  >>> find_all(lst, lambda x: x % 2 == 0, 2)
  -> [4]

  python 3:
  >>> lst = [1, 2, 3, 4, 5]
  >>> find_all(lst, lambda x: x % 2 == 0)
  -> [2, 4] <generator>
  >>> find_all(lst, lambda x: x % 2 == 0, 2)
  -> [4] <generator>
  '''
  if end == None:
    end = len(seq)

  return filter(func, islice(seq, start, end))

def find_index(seq, func, from_index = 0):
  '''
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
  '''
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

def groupby(seq, key):
  '''
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
  ... {'name': 'Sam' 'gender': 'male'},
  ... {'name': 'John' 'gender': 'male'},
  ... {'name': 'Jane' 'gender': 'female'},
  ... {'name': 'Chase' 'gender': 'male'},
  ... {'name': 'Melanie' 'gender': 'female'}]
  >>> groupby(people, 'gender')
  -> {
      'male': [
        {'name': 'Sam' 'gender': 'male'},
        {'name': 'John' 'gender': 'male'},
        {'name': 'Chase' 'gender': 'male'}
      ], 
      'female': [
        {'name': 'Jane' 'gender': 'female'},
        {'name': 'Melanie' 'gender': 'female'}
      ]
     }
  '''
  dct = {}
  get = dct.get
  if callable(key):
    for item in seq:
      val = key(item)
      if get(val) != None:
        dct[val].append(item)
      else:
        dct[val] = [item]
  else:
    for item in seq:
      val = item[key]
      if get(val) != None:
          dct[val].append(item)
      else:
        dct[val] = [item]
  return dct

def head(seq):
  '''
  Description
  ----------
  Return the first value in the sequence.

  Parameters
  ----------
  seq : (list or tuple or string) - sequence to get first value of

  Returns
  ----------
  any - first value of the sequence

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5]
  >>> head(lst)
  -> 1
  '''
  return seq[0]

def index_of(seq, value, from_index = 0):
  '''
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
  '''
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

def initial(seq):
  '''
  Description
  ----------
  Create a generator of all the values in a sequence except the last.

  Parameters
  ----------
  seq : (list or tuple or set or string) - sequence to take values from

  Returns
  ----------
  generator - a generator containing all values of the sequence but the last

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5]
  >>> initial(lst)
  -> [2, 3, 4, 5] <generator>
  '''
  return islice(seq, 0, len(seq)-1)

def intersection(*seqs):
  '''
  Description
  ----------
  Creates a generator containing values found in all sequences.

  Parameters
  ----------
  *seqs : (list or tuple or set or dict) - sequences to pull common values from

  Returns
  ----------
  generator - a generator containing values found in all sequences

  Example
  ----------
  >>> intersection([1, 2, 3, 4], [3, 4, 5], [2, 3, 4, 5])
  -> [3, 4] <generator>
  '''
  if len(seqs) <= 1:
    return

  def helper(seqs, value):
    for seq in seqs:
      if not value in seq:
        return False
    return True

  for value in seqs[0]:
    if helper(islice(seqs, 1, len(seqs)), value):
      yield value

def join(seq, separator = ','):
  '''
  Description
  ----------
  Concatenate all values in a sequence into a string separated by the separator value.

  Parameters
  ----------
  seq : (list or tuple) - sequence of values to concatenate\n
  separator : any, optional - value to separate the values in the sequence (default is ',')

  Returns
  ----------
  str - a string of the values concatenated and separated by the separator value

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5]
  >>> join(lst)
  -> '1,2,3,4,5'
  >>> join(lst, '-')
  -> '1-2-3-4-5'
  '''
  string = ''
  i = 0
  length = len(seq)
  while i < length:
    if i == length-1:
      string = string + str(seq[i])
    else :
      string = string + str(seq[i]) + str(separator)
    i = i + 1
  return string

def last(seq):
  '''
  Description
  ----------
  Return the last value in the sequence.

  Parameters
  ----------
  seq : (list or tuple or string) - sequence to return last value of

  Returns
  ----------
  any - the last value in the sequence

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5]
  >>> last(lst)
  -> 5
  '''
  return seq[-1]

def merge(*seqs):
  '''
  Description
  ----------
  Create a generator that contains one instance of all values from the sequences.

  Parameters
  ----------
  *seqs : (list or tuple or set or dict or string) - sequences to merge

  Returns
  ----------
  generator - generator containing values from the sequences

  Example
  ----------
  >>> merge([1, 2, 3, 4, 5, 5], (1, 2, 3, 5, 6, 7), {'a', 'b', 'c'})
  -> [1, 2, 3, 4, 5, 6, 7, 'a', 'c', 'b'] <generator>
  '''
  lst = []
  append = lst.append

  for seq in seqs:
    for item in seq:
      if not item in lst:
        append(item)
        yield item

def pipe(data, *funcs):
  '''
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
  '''
  value = data
  for func in funcs:
    value = func(value)
  return value

def pull(lst, *pull_vals):
  '''
  Description
  ----------
  Remove values from the list.\n
  Mutates the list.

  Parameters
  ----------
  lst : list - list to remove values from\n
  *pull_vals : any - values to remove

  Returns
  ----------
  None

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 2, 4, 5, 6, 1]
  >>> pull(lst, 2, 4, 1)
  >>> lst
  -> [3, 5, 6]
  '''
  remove = lst.remove

  for value in pull_vals:
    while value in lst:
      remove(value)

def pull_all(lst, pull_vals):
  '''
  Description
  ----------
  Remove values from the list.\n
  Mutates the list.

  Parameters
  ----------
  lst : list - list to remove values from\n
  pull_vals : (list or tuple or set) - sequence of values to remove

  Returns
  ----------
  None

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 2, 4, 5, 6, 1]
  >>> pull(lst, [2, 4, 1])
  >>> lst
  -> [3, 5, 6]
  '''
  remove = lst.remove

  for value in pull_vals:
    while value in lst:
      remove(value)
  
def pull_at(lst, *pull_indices):
  '''
  Description
  ----------
  Remove values at all specified indices.\n
  Mutates the list.

  Parameters
  ----------
  lst : list - list to remove values from\n
  *pull_indices : int - indices to remove

  Returns
  ----------
  None

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5, 6, 7]
  >>> pull_at(lst, 0, 2, 4)
  >>> lst
  -> [2, 4, 6, 7]
  '''
  lst_len = len(lst)
  offset = 0
  i = 0

  for index in pull_indices:
    if index <= lst_len-1:
      del lst[index-offset]
      try:
        if index < pull_indices[i+1]:
          offset = offset + 1
      except:
        pass
      i = i + 1

def pull_all_at(lst, pull_indices):
  '''
  Description
  ----------
  Remove values at all specified indices.\n
  Mutates the list.

  Parameters
  ----------
  lst : list - list to remove values from\n
  pull_indices : (list or tuple or set) - sequence of indices to remove

  Returns
  ----------
  None

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5, 6, 7]
  >>> pull_at(lst, [0, 2, 4])
  >>> lst
  -> [2, 4, 6, 7]
  '''
  lst_len = len(lst)
  offset = 0
  i = 0

  for index in pull_indices:
    if index <= lst_len-1:
      del lst[index-offset]
      try:
        if index < pull_indices[i+1]:
          offset = offset + 1
      except:
        pass
      i = i + 1

def remove(seq, *remove_vals):
  '''
  Description
  ----------
  Remove values from the sequence.

  Parameters
  ----------
  seq : (list or tuple or set or dict) - sequence to remove values from\n
  *remove_vals : any - values to remove

  Returns
  ----------
  generator - generator containing all values not removed from the sequence

  Example
  ----------
  >>> remove([1, 2, 3, 4], 2, 1)
  -> [3, 4] <generator>
  '''
  for item in seq:
    if not item in remove_vals:
      yield item

def remove_all(seq, remove_vals):
  '''
  Description
  ----------
  Remove values from the sequence.

  Parameters
  ----------
  seq : (list or tuple or set or dict) - sequence to remove values from\n
  *remove_vals : (list or tuple or set) - sequence of values to remove

  Returns
  ----------
  generator - generator containing all values not removed from the sequence

  Example
  ----------
  >>> remove([1, 2, 3, 4], [2, 1])
  -> [3, 4] <generator>
  '''
  for item in seq:
    if not item in remove_vals:
      yield item

def remove_at(seq, *remove_indices):
  '''
  Description
  ----------
  Remove values at specified indices from the sequence.

  Parameters
  ----------
  seq : (list or tuple) - sequence to remove values from\n
  *remove_indices : int - indices to remove

  Returns
  ----------
  generator - a generator containing all values not removed from the sequence

  Example
  ----------
  >>> tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
  >>> remove_at(tup, 0, 3, 1, 5)
  >>> ['c', 'e', 'g'] <generator>
  '''
  index = 0
  while index < len(seq):
    if not index in remove_indices:
      yield seq[index]
    index = index + 1

def remove_all_at(seq, remove_indices):
  '''
  Description
  ----------
  Remove values at specified indices from the sequence.

  Parameters
  ----------
  seq : (list or tuple) - sequence to remove values from\n
  remove_indices : (list or tuple or set) - sequence of indices to remove

  Returns
  ----------
  generator - a generator containing all values not removed from the sequence

  Example
  ----------
  >>> tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
  >>> remove_all_at(tup, [0, 3, 1, 5])
  >>> ['c', 'e', 'g'] <generator>
  '''
  index = 0
  while index < len(seq):
    if not index in remove_indices:
      yield seq[index]
    index = index + 1

def subset(seq, start = 0, end = None):
  '''
  Description
  ----------
  Create a subset of the sequence.

  Parameters
  ----------
  seq : (list or tuple or set or dict) - sequence of values to subset\n
  start : int, optional - start index (default is 0)\n
  end : int, optional - end index (not included) (default is None = len(seq))

  Returns
  ----------
  generator - generator of the subset of values

  Examples
  ----------
  >>> lst = [1, 2, 3, 4, 5, 6, 7]
  >>> subset(lst, 2)
  -> [3, 4, 5, 6, 7] <generator>
  >>> subset(lst, 3, 5)
  -> [4, 5] <generator>
  '''
  if end == None:
    end = len(seq)
  
  return islice(seq, start, end)

def some(seq, func):
  '''
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
  '''
  for item in seq:
    if func(item):
      return True
  return False

def tail(seq):
  '''
  Description
  ----------
  Return all values in the sequence except the first.

  Parameters
  ----------
  seq : (list or tuple or set or dict) - sequence of values

  Returns
  ----------
  generator - a generator containing all values of the sequence but the first

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5, 6]
  >>> tail(lst)
  -> [2, 3, 4, 5, 6] <generator>
  '''
  return islice(seq, 1, len(seq))

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
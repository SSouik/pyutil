from itertools import islice
                       
def chunk(seq, n):
  '''
  Description
  ----------
  Create a generator of values split into 'n' length.\n
  If the sequence cannot be split evenly, then the\n 
  last group will be the remaining values in the sequence.

  Parameters
  ----------
  seq : (list or tuple or set or string) - sequence to chunk values of\n
  n : int - number to group by

  Returns
  ----------
  generator - a generator of lists of length 'n'\n 
  containing the original sequence's values

  Example
  ----------
  >>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  >>> chunk(lst, 3)
  -> [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]] <generator>
  '''
  if not (
    type(seq) is list
    or type(seq) is tuple
    or type(seq) is set
    or type(seq) is str
  ):
    raise TypeError('param \'seq\' must be a list, tuple, set, or string')

  if not type(n) is int:
    raise TypeError('param \'n\' must be an integer: 0 <= n <= sys.maxsize')

  if n < 0:
    raise ValueError('param \'n\' must be an integer: 0 <= n <= sys.maxsize')

  if n == 0:
    yield seq
    return

  start = 0
  end = n

  while n != 0 and end < len(seq):
    yield list(map(lambda x: x, islice(seq, start, end)))
    start = start + n
    end = end + n
  
  yield list(map(lambda x: x, islice(seq, start, end)))

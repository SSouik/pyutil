from itertools import islice

########################################################
#                                                      #
# The following functions operate on Python sequences. #
# (lists, tuples, sets, dictionaries and strings)      #
#                                                      #
########################################################
                                      
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
  if not type(n) is int:
    raise TypeError('param \'n\' must be an integer: 0 <= n <= sys.maxsize')


  start = 0
  end = n

  while end < len(seq):
    yield list(map(lambda x: x, islice(seq, start, end)))
    start = start + n
    end = end + n
  
  yield list(map(lambda x: x, islice(seq, start, end)))


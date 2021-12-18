def compact(seq):
  '''
  Description
  ----------
  Remove all falsey values from the sequence.

  Parameters
  ----------
  seq : (list or tuple or set) - sequence to remove falsey values from

  Returns
  ----------
  python 2:
  list - a list with all falsey values removed\n

  python 3:
  generator - a generator with all falsey values removed

  Examples
  ----------
  python 2:
  >>> lst = [1, 2, 3, [], 0, 'hello', False, '']
  >>> compact(lst)
  -> [1, 2, 3, 'hello']

  python 3:
  >>> lst = [1, 2, 3, [], 0, 'hello', False, '']
  >>> compact(lst)
  -> [1, 2, 3, 'hello'] <generator>
  '''
  if not (
    type(seq) is list
    or type(seq) is tuple
    or type(seq) is set
  ):
    raise TypeError('param \'seq\' must be a list, tuple, or set')

  return filter(bool, seq)


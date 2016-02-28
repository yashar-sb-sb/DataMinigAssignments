import random

def _randomizedSelection(a, p):
  random.shuffle(a)
  i = 0
  j = 0
  k = len(a)
  while k > j:
    if a[j] < a[i]:
      a[i], a[j] = a[j], a[i]
      j += 1
      i += 1
    elif a[j] > a[i]:
      k -= 1
      a[j], a[k] = a[k], a[j]
    else:
      j += 1
  
  if p < i:
    a[:i] = _randomizedSelection(a[:i], p)
  elif p >= j:
    a[j:] = _randomizedSelection(a[j:], p-j)
  return a


def randomizedSelection(a, p, **args):
  """
  a has to be a list
  args could have l or r or both
  if non of l nor r is presented then the function will perform the operation on the whole of a
  if only l is presented the operation will be performed on range [l:]
  if only r is presented the operation will be performed on range [:r]
  if both are presented the operation will be performed on range [l:r]
  """
  l = args['l'] if 'l' in args else 0
  r = args['r'] if 'r' in args else len(a)
  a[l:r] = _randomizedSelection(a[l:r], p-l)



def deterministicSelection(a, p, **args):
  """
  a has to be a list
  args could have l or r or both
  if non of l nor r is presented then the function will perform the operation on the whole of a
  if only l is presented the operation will be performed on range [l:]
  if only r is presented the operation will be performed on range [:r]
  if both are presented the operation will be performed on range [l:r]
  """

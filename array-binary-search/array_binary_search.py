def binary_search(lst, val):
  i = 0
  for x in lst:
    if x == val:
      return i
    i += 1
  else:
    return -1
def index(array, n):
    if len(array) < n:
      return -1
    else:
      return array[n]**n

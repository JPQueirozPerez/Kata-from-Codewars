def men_from_boys(arr):
    even = []
    odd = []
    for i in arr:
      if i not in even and i not in odd:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return sorted(even)+sorted(odd, reverse=True)

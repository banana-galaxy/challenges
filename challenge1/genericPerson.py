def solution(arr, newdim=64):
  # Not the most elegant, but...
  scalef = int(newdim / len(arr))
  new_arr = []
  for i in arr:
    hold = []
    for j in i:
      for x in range(scalef):
        hold.append(j)
    for x in range(scalef):
      new_arr.append(hold)
  return new_arr
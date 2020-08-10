def solution(list):
  if len(list) == 0:
    return 0,list
  else:
    count = 0
    for n in range(len(list)-1):
      while list[n] >= list[n+1]:
        list[n+1] = list[n+1] + 1
        count += 1
    return count,list
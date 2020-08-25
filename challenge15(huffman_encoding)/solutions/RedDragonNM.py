def solution(string):
  lst = string.split(" ")
  count = len(set(lst)) + 1
  new_string = ""

  for s in lst:
    new_string += "{} ".format(count - lst.count(s))

  return new_string.strip()
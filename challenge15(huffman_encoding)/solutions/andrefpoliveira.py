def solution(s):
  words = s.split(" ")
  dic = {}
  for i in words: dic[i] = dic.get(i, 0) + 1
  order = [x for (x, _) in sorted(dic.items(), key=lambda item: item[1], reverse=True)]
  return " ".join([str(order.index(w)+1) for w in words])
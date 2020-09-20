def solution(k):
  red,yellow =0,0
  for m in range(k+1) :

    if m % 2 ==0:
      red += m**2
    else:
      yellow += m**2
  return (red-yellow)
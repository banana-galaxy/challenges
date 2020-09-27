def solution(a):
  divisors = [a]
  answer = False
  for i in range(1, int((a/2)+1)):
    if(a % i == 0):
      divisors.append(i)
  if(len(divisors) == 3):
     answer = True
  return answer
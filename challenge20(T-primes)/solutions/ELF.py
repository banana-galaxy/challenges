def solution(x, a=0):
    for i in range(1,x+1):
        if x%i==0:
          a+=1
    return True if a==3 else False
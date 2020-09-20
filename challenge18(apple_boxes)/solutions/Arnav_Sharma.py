def solution(k):
    sy = sum(i**2 for i in range(1,k+1,2))
    sr = sum(i**2 for i in range(2,k+1,2))
    return sr-sy
python
def solution(n):
    for k in range(n):
        y=len([k for k in range(1,n+1) if not n %k])
    if y == 3:
        return True
    else:
        return False
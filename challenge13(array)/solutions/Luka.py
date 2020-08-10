def solution(A):
    n=0
    for i in range(1,len(A)):
        if A[i-1] >= A[i]:
            n += A[i-1]-A[i]+1
            A[i] += A[i-1]-A[i]+1
    return n
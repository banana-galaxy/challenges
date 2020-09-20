def solution(k):
    ya,ra=0,0
    for i in range(1,k+1):
        if i%2!=0:
            ya+=i*i
        else:
            ra+=i*i
    return ra-ya
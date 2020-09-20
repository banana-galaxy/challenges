def solution(k):
    r_apple,y_apple=(a*a for a in range(1,(k+1)) if a%2==0),(j*j for j in range(1,(k+1)) if j%2!=0)
    return (sum(r_apple)-sum(y_apple))
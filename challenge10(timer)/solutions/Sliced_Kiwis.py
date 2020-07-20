def lateRide(n):
    ans=n//60
    ans=(ans*100)+(n%60)

    sum=0
    for digit in str(ans):
        sum +=int(digit)

    return sum
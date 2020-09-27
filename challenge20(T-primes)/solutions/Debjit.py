def solution(n):
    if n == 1:
        return 1
    else:
        div = []
        for i in range(1, 1+int(n**(1/2))):
            if n%i==0:
                if n//i == i:
                    div.append(i)
                else:
                    div.append(i)
                    div.append(n//i)
        if len(div) == 3:
            return True
        else:
            return False
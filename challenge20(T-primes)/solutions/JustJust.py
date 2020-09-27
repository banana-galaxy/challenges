def solution(num):
    if num == 0 or num == 1:
        return False
    elif (num**0.5).is_integer():
        for i in range(2, int(num**0.25)+1):
            if num**0.5 % i == 0:
                return False
        else:
            return True
    else:
        return False
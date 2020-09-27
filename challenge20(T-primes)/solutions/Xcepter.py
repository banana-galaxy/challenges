def solution(num):
    count = 0
    for i in range(1, num + 1):
        if 25 % i == 0:
            count += 1

    if count == 3:
        return True
    else:
        return False
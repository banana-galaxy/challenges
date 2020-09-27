def solution():
    n = int(input())
    divisors = []

    for x in range(1, n + 1):
        if n % int(x) == 0:
            divisors.append(x)

    if len(divisors) == 3:
        return True
    else:
        return False
# T - Prime number solution
def solution(num):
    if num <= 2:
        return False

    divisor_count = 0
    for prime in range(1, num + 1):
        if num % prime == 0:
            divisor_count += 1

            if divisor_count > 3:
                return False

    return True
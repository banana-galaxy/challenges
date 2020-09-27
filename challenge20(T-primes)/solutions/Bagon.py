def solution(num: int) -> bool:
    return sum(not num % i for i in range(1, num + 1)) == 3
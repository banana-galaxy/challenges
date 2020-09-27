def solution(num):
    divors = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divors += 1
            print(f"I:{i}, Divors: {divors}, Num: {num}")
    return divors == 3
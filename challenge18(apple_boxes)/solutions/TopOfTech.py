def solution(k):
    red_apples = [i*i for i in range(1, k+1) if i % 2 == 0]
    yellow_apples = [i*i for i in range(1, k+1) if i % 2 != 0]
    return sum(red_apples) - sum(yellow_apples)
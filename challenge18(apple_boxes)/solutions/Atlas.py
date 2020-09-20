def solution(k):
    answer = 0
    for i in range(k + 1):
        answer += int((i % 2 * "-") + str(i * i))
    return answer
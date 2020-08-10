def solution(ls):
    ans = 0
    for i in range(1, len(ls)):
        if ls[i-1] >= ls[i]:
            ans += ls[i-1] - ls[i] + 1
            ls[i] = ls[i-1] + 1

    return ans
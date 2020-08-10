def solution(numList: list):
    ans = 0
    firstElement = numList[0]
    for num in numList[1:]:
        if num <= firstElement:
            ans += firstElement - num + 1
            firstElement += 1
        else:
            firstElement = num
    return ans
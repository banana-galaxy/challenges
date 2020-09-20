def solution(k):
    red_apples, yellow_apples, nums = 0, 0, []

    for x in range(k):  nums.append(x + 1)

    for num in nums:
        if num % 2 == 0:
            red_apples += num ** 2
        elif num % 2 == 1:
            yellow_apples += num ** 2

    return red_apples - yellow_apples
def solution(k):
    def is_odd(x):
        if x % 2 != 0:
            return True
        else:
            return False

    yellow_sum = 0
    red_sum = 0

    for i in range(1, k+1):
        if is_odd(i):
            yellow_sum += (i*i)
        else:
            red_sum += (i*i)

    difference = red_sum - yellow_sum

    return difference
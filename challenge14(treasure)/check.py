def solution(value1, weight1, value2, weight2, maxW):
    if weight1+weight2 <= maxW:
        return value1+value2
    elif weight1 <= maxW and weight2 <= maxW:
        return max(value1, value2)
    elif weight1 <= maxW:
        return value1
    elif weight2 <= maxW:
        return value2
    else:
        return 0

if __name__ == '__main__':
    #print(solution([-1000, 0, -2, 0]))

    粘贴 = "hi"
    print(粘贴)
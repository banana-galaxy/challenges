def solution(arr, count=0):
    copy = arr.copy()

    for i in range(len(arr)):
        a, b = arr[i], arr[i - 1]
        if i != 0:
            if a <= b: a = a + (abs(a - b) + 1)

    for i in range(len(arr)): count += arr[i] - copy[i]

    return count
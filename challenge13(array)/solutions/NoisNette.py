def solution(arr):
    a = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            while arr[i] <= arr[i-1]:
                arr[i] += 1
                a += 1
    return a
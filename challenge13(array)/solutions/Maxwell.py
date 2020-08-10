def solution(arr):
    counter = 0
    for i in range(len(arr)-1):
        while arr[i+1] <= arr[i]:
            arr[i+1] += 1
            counter += 1
    return counter
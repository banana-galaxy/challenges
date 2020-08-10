def solution(arr):
    sol = 0
    for i in range(1, len(arr)):
        if (arr[i] <= arr[i-1]):
            sol += arr[i-1] + 1 - arr[i]
            arr[i] = arr[i-1]+1

    return sol
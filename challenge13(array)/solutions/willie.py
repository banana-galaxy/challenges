def solution(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            calc = abs(arr[i] - arr[i-1]) + 1
            count += calc
            arr[i] += calc

    return count
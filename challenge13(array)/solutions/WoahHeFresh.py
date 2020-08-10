def solution(arr):
    sum = 0
    for i, v in enumerate(arr):
        if i == 0: continue
        else:
            while test[i] <= test[i-1]:sum+=1;test[i]+=1

    return sum
def solution(li):
    counter = 0
    for i in range(len(li)):
        if i > 0:
            while li[i] <= prev:
                li[i] += 1
                counter += 1
        prev = li[i]
    print(li)
    return counter
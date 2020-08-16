def solution(v1, w1, v2, w2, W):
    if W < w1 and W < w2:
        return 0

    elif W >= w1 and W < w2:
        return v1

    elif W >= w2 and W < w1:
        return v2

    elif W >= w1 and W >= w2 and W < w1 + w2:
        if v1 > v2:
            return v1
        else:
            return v2

    elif W >= w1 + w2:
        return v1 + v2
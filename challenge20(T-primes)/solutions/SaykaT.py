def solution(k):
    cache = dict()

    if k in cache:
        return cache[k]
    else:
        root = k**0.5
        if root.is_integer():
            for i in range(2, int(root**0.5)+1):
                if k % i == 0:
                    cache[k] = False
                    break
            if k not in cache:
                cache[k] = root > 1
        else:
            cache[k] = False

        return cache[k]
# @alex-galaxy#5128 @HETHAT#5372 @M7MD#2996 
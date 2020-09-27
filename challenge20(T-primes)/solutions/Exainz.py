def solution(x):
    root = x ** 0.5
    if x in [0, 1]:
        return 0
    if root.is_integer():
        for i in range(2, int(root ** 0.5)):
            if root % i == 0:
                return 0
        return 1
    return 0
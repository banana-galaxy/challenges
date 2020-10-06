def solution(a, b, n):

    x1 = ord(a[0])
    x2 = ord(b[0])
    y1 = int(a[1])
    y2 = int(b[1])

    if n >= 2 and (x1 + y1 + x2 + y2) % 2 == 0:
        return True
    elif n == 1 and abs(x1 - x2) == abs(y1 - y2):
        return True
    elif a == b:
        return True
    else:
        return False
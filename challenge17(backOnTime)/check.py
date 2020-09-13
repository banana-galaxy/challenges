def solution(n):
    if n.count('n') == n.count('s'):
        if n.count('e') == n.count('w'):
            if len(n) <= 10:
                return True
    return False
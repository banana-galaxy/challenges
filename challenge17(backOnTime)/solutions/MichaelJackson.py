def solution(n):
    if len(n) > 10:return False
    elif n.count('n') == n.count('s') and n.count('e') == n.count('w'):return True
    return False
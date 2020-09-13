def solution(list):
    if len(list) % 2 == 1:
        return False
    if list.count('n') != list.count('s'):
        return False
    if list.count('e') != list.count('w'):
        return False
    if len(list) > 10:
        return False
    return True
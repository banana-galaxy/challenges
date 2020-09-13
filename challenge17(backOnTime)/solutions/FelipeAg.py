def solution(steps):
    if len(steps) > 10:
        return False
    elif steps.count('n') == steps.count('s') and steps.count('e') == steps.count('w'):
        return True
    return False
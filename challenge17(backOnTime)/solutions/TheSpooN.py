def solution(path: list) -> bool:
    n = len(path)
    if n > 10:
        return False
    x, y = 0, 0
    for dir in path:
        if dir == 'n': x -= 1
        if dir == 's': x += 1
        if dir == 'e': y -= 1
        if dir == 'w': y += 1

    return (x == 0 and y == 0)
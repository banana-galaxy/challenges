def solution(a: str, b: str, moves: int):
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # it's the same square
    if moves == 0 and a == b:
        return True
    elif moves == 0:
        return False

    a_rank = int(a[1])
    b_rank = int(b[1])

    a_file = files.index(a[0])
    b_file = files.index(b[0])

    # they're on the same diagonal
    if moves == 1 and abs(a_rank - b_rank) == abs(a_file - b_file):
        return True
    elif moves == 1:
        return False

    # they're on the same color square
    if moves >= 2 and (a_rank + b_rank + a_file + b_file) % 2 == 0:
        return True

    return False
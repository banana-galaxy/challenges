def solution(pos1, pos2, moves):
    if pos1 == pos2:
        return True
    elif moves > 1:
        value1 = ord(pos1[0]) - 96 + int(pos1[1])
        value2 = ord(pos2[0]) - 96 + int(pos2[1])

        if value1 % 2 == value2 % 2:
            return True
    elif moves == 1:
        v1 = abs(int(pos2[1]) - int(pos1[1]))
        v2 = abs(ord(pos2[0]) - ord(pos1[0]))

        if v1 == v2:
            return True
    return False
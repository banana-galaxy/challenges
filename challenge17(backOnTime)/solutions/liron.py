def solution(path):
    if len(path)>10 or len(path)%2 != 0:
        return False
    south = len([x for x in path if x == 's'])
    north = len([x for x in path if x == 'n'])
    east = len([x for x in path if x == 'e'])
    west = len([x for x in path if x == 'w'])
    return south == north and east == west
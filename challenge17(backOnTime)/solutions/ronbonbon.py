def solution(walk):
    if len(walk)>10:
        return False
    lencheck = 0
    for i in walk:
        if   i == 'n':
            lencheck+=11
        elif i == 's':
            lencheck-=11
        elif i == 'e':
            lencheck+=13
        elif i == 'w':
            lencheck-=13
    if lencheck==0: return True
    return False  
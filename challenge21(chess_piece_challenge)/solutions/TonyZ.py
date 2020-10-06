def solution(start, end, moves):
    _start = getPosition(start)
    _end = getPosition(end)
    _dist = (_end[0] - _start[0],_end[1] - _start[1])
    if _dist == (0,0):
        return(moves>=0)
    elif _dist[0] == _dist[1]:
        return(moves>=1)
    elif not bool((_dist[0] - _dist[1])%2):
        return(moves>=2)
    return False

def getPosition(x):
    return(ord(x[0])-97,int(x[1]))
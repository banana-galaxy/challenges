def whichExit(M):
    r = [row for row in M if 0 in row][0]
    spot = r.index(0)
    right = sum([1 for x in r[spot:] if x == 1])
    left = sum([1 for x in r[:spot] if x == 1])
    return ['left', 'right', 'same'][ (right < left) + (left == right)*2]
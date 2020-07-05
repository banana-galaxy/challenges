def whichExit(_list):
    for row in _list:
        if 0 in row:
            a = row.count(1) - row[:row.index(0)].count(1) * 2
            if a > 0:
                return 'left'
            if a < 0:
                return 'right'
            else:
                return 'same'
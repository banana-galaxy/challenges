def erange(x, y=None, z=None):
    if y == None and z == None:
            w = 0
            while x!=0:
                yield w
                x -= 1
                w += 1
    elif z == None and y > x:
        while x != y:
            yield x
            x += 1
    elif y and z:
        z = int(z)
        while x-1 != y and y > x and z < y:
            yield x
            x += z        
        
def numerate(x, y=0):
    for i in erange(len(x)):
        yield y, x[i]
        y += 1
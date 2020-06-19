def erange(start, *args):
    if not type(start) == int:
        raise TypeError("Only integer inputs allowed")
    if not args:
        end = start
        start = 0
        stepsize = 1
    if len(args) == 1:
        if not type(args[0]) == int:
            raise TypeError("Only integer inputs allowed")
        end = args[0]
        stepsize = 1
    if len(args) == 2:
        if not type(args[0]) == int and type(args[1]) == int:
            raise TypeError("Only integer inputs allowed")
        end, stepsize = args[:2]
        if not stepsize:
            print("stepsize has to be non-zero")
            return;
        if (stepsize < 0 and start < end) or (stepsize > 0 and start > end):
            return [];
    if len(args) > 2:
        print("too many arguments arguments")
        return ;
    i = 0
    output = []
    if start < end:
        while start + stepsize * i < end:
            output += [start + stepsize * i]
            i += 1
    elif start > end:
        while start + stepsize * i > end:
            output += [start + stepsize * i]
            i += 1
    return output

def numerate(R, index = 0):
    try:
        list(R)
    except:
        print("numerate only accepts lists as input")
        return;
    out = []
    for x in R:
        out += [[index, x]]
        index += 1
    return out
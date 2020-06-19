def numerate(obj, index = 0):
    if index == 0: idx = 0
    else: idx = index
    for item in obj: yield idx, item; idx += 1

def erange(*args):
    current, start, stop, step = 0, 0 , 0, 1

    if len(args) > 3: raise NotImplementedError
    elif len(args) == 3: start, stop, step = args[0], args[1], args[2]
    elif len(args) == 2: start, stop = args[0], args[1]
    elif len(args) == 1: stop = args[0]
    else: raise NotImplementedError
    current = current + start
    if stop > start and step > 0:
        while current < stop and current >= start: yield current; current += step
    elif start > stop and step < 0:
        while current > stop and current <= start: yield current; current += step
    else: return ''
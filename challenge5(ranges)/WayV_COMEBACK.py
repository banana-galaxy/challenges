def erange(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start

    for n in [start, step, stop]:
        if type(n) is not int:
            raise TypeError("'{}' object cannot be interpreted as an integer".format(str(type(n)).split("'")[1]))

    if step == 0:
        raise ValueError('erange() arg 3 must not be zero')
    elif (step > 0 and start < stop) or (step < 0 and start > stop): 
        l = []
        c = start
        while True:
            l.append(c)
            c += step

            if (step > 0 and c >= stop) or (step < 0 and c <= stop):
                break

        return l
    else:
        return []


def numerate(ls, start=0):
    try:
        iter(ls)
    except Exception as e:
        raise e

    if type(start) is not int:
        raise TypeError("'{}' object cannot be interpreted as an integer".format(str(type(start)).split("'")[1]))

    l = []
    for element in ls:
        l.append((start, element))
        start += 1

    return l
def erange(start, end=None, step=1):
    result = []
    if end == None:
        end = start
        start = 0
    count = start
    if step > 0:
        while count < end:
            result.append(count)
            count += step
    elif step < 0:
        while count > end:
            result.append(count)
            count += step
    return result

def numerate(iterator, start=0):
    result = []
    count = start
    for item in iterator:
        result.append((count, item))
        count += 1
    return result
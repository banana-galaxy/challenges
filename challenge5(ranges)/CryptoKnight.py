def erange(start=0, stop=None, step=1):
    difference, incrementer = (start, 0 - step) if stop is None else ((stop - 1) - start + step, start - step)
    return [(incrementer := incrementer + step) for _ in [''] * int(format(difference / step, '.0f'))]


def numerate(list, start=0):
    return [(list.index(item) + start, item) for item in list]
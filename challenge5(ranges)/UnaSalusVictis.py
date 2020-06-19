def erange(*args):
    # input validation
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError("'{}' object cannot be interpreted as an integer".format(type(arg)))

    if len(args) > 3:
        raise TypeError(f"erange expected at most 3 arguments, got {len(args)}")

    # begin making sure all the settings for iteration are correct
    if len(args) == 1:
        start = 0
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]

    if len(args) < 3:
        step = 1
    else:
        step = args[2]

    if step == 0:
        raise ValueError("erange() arg 3 must not be zero")

    # neither of these scenarios are computable and will simply return an empty list
    if stop < start and step > 0:
        return []
    elif stop > start and step < 0:
        return []

    # now the real iteration begins
    if start < stop:
        while start < stop:
            yield start
            start += step

    elif start > stop:
        while start > stop:
            yield start
            start += step

    elif start == stop:
        return []


def numerate(in_list, base = 0):
    if not isinstance(base, int):
        raise ValueError("var base must be of type `int`")

    for item in in_list:
        yield (base, item)
        base += 1
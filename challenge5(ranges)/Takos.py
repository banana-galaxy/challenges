def erange(*args):
    if len(args) > 3 or len(args) == 0:
        raise TypeError(
            f"erange expected {3 if len(args) > 3 else 1} arguments, got {len(args)}")
    if any([type(i) != int for i in args]):
        raise TypeError("all arguments must be of type 'int'")

    start = args[0] if len(args) >= 2 else 0
    stop = args[0] if len(args) == 1 else args[1]
    step = args[2] if len(args) == 3 else 1

    if step == 0:
        raise ValueError("step arg must not be 0")

    i = start
    while (i < stop) if step > 0 else (i > stop):
        yield i
        i += step


def numerate(elements, start=0):
    i = 0
    for v in elements[start:]:
        yield (i, v)
        i += 1
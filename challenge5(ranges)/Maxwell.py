def erange(*args):
    for arg in args:  # verify that every argument is an integer
        if type(arg) != int:
            raise TypeError("arguments must be integers")

    if len(args) == 1:  # one argument, goes from 0 to arg
        if args[0] <= 0:
            return []
        i, lst = 0, []
        while i != args[0]:
            yield i
            i += 1

    elif len(args) == 2:  # two arguments, start and stop
        if args[1] <= args[0]:
            return []
        i, lst = args[0], []
        while i < args[1]:
            yield i
            i += 1

    elif len(args) == 3:  # 3 arguments, start, stop, step
        if (args[1] >= args[0] and args[2] < 0) or (args[1] <= args[0] and args[2] > 0):
            return []
        i, lst = args[0], []
        if args[2] < 0:  # negative step
            while i > args[1]:
                yield i
                i += args[2]
        elif args[2] > 0:  # positive step
            while i < args[1]:
                yield i
                i += args[2]
        elif args[2] == 0:
            raise ValueError("erange() arg 3 must not be 0")

    else:  # no arguments or more than 3 arguments raises an error
        raise SyntaxError("one, two or three arguments supported, no more, no less")


def numerate(iterable, start=0):
    if type(start) != int:
        raise TypeError('start should be of type int')
    index = 0 + start
    for element in iterable:
        yield(index, element)
        index += 1
def erange(*args):
    """
    Makes a sequence of ints customized by the parameters.
    STOP: The last number of your list.
    START: The first number in your list. Defaults to 0
    STEP: How far away each number should be(any better explanations?) Defaults to 1.
    """ 
    if len(args) == 0 or len(args) > 3: raise TypeError(f"Erange takes from 1 to 3 arguments, got {len(args)}")
    for v in args:
        if type(args[args.index(v)]) != int: raise TypeError(f"Erange only accepts 'int' type variables, got {type(args[args.index(v)])}.")
    start, stop, step = args[0] if len(args) > 1 else 0, args[1] if len(args) > 1 else args[0], args[2] if len(args) > 2 else 1
    if step == 0: raise ValueError("Arg3 (step) can't be zero.")
    i, d = start, 1 if step>0 else -1
    if ((start*d-stop*d) < stop*d) and (i*d < stop*d):
        yield start
        i += step
    while (i*d < stop*d):
        yield i
        i += step

def numerate(yourIter, start=0):
    """
    Enumerates each entry in any iterable object.
    YOURITER: Any iterable object you want.(lists, dicts,tuples, etc)
    START: The number with which it will start enumerating. Defaults to 0
    """
    if type(start) != int: raise TypeError(f"Numerate only accepts 'int' type variables, got {type(start)}.")
    i = start
    for r in yourIter:
        yield i, r
        i += 1
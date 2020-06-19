def erange(*args):
    #length
    if len(args) not in [1,2,3]:
        raise TypeError(f"erange expected 1 to 3 arguments, got {len(args)}")
    
    #define start,stop,step
    elif len(args) == 1:
        start,stop,step = 0,args[0],1
    elif len(args) == 2:
        start,stop,step = args[0],args[1],1
    elif len(args) == 3:
        if args[2] == 0:
            raise ValueError("erange() step must not be zero")
        start,stop,step = args
    
    #type
    if type(start)!=int or type(stop)!=int or type(step)!=int:
        raise TypeError("all args should be integers")
        
    #main
    i = start
    while True:
        if (i >= stop and step > 0) or (i <= stop and step < 0):
            break
        yield i
        i += step
        

def numerate(iterable,start=0):
    if not iter(iterable):
        raise TypeError(f"{type(iterable).__name__} object is not iterable")
    
    if not type(start) == int:
        raise TypeError(f"arg 'start' should be integer, not {type(start)}")
        
    c = start
    i = 0
    while True:
        for iterobject in iterable:
            yield (i+c,iterobject)
            i += 1
        break
def numerate(a,b:int=0):
    for x in a :yield ((b,x));b += 1
def erange(a:int,b:int=None,step:int=1):
    if step == 0 or not (all(list(map(lambda x:type(x)==int,[a,b,step]))) if b!=None else type(a)==int) :raise ValueError("step arg must not be 0") if step == 0 else TypeError("only 'int' type is acceptable")
    d =(0 if b is None else a)
    while (d < a if b is None else d < b) if step > 0 else d > b:yield d ;d += step
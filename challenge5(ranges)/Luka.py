def erange(start=None,stop=None,c=1):
    li=[]
    number=0
    if stop!=None:
        if isinstance(start,int)==False or isinstance(stop,int)==False or isinstance(c,int)==False:
            raise TypeError("range only takes integer as an argument")
    else:
        if isinstance(start,int)==False or isinstance(c,int)==False:
            raise TypeError("range only takes integer as an argument")
    if start!=None and stop!=None and c==1:
        number=start
        while number!=stop:
            li.append(number)
            number+=c
        return li

    
    elif start!=None and stop!=None and c!=1:
        number=start
        if c==0:raise ValueError("range() arg 3 must not be zero")
        if c>0:
            while number<stop:
                li.append(number)
                number+=c
        if c<0:
            while number>stop:
                li.append(number)
                number+=c
        return li

    elif isinstance(start,int):
        while number!=start:
            li.append(number)
            number+=1
        return li

def numerate(a):
    li=[]
    index=0
    try:
        for i in a:
            li.append((index,i))
            index+=1
    except:raise TypeError("given variable is not iterable")
    return li
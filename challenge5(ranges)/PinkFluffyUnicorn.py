def numerate(list, start=0):
    listElements = []
    for element in list:
        temp = tuple((start, element))
        listElements.append(temp)
        start = start + 1
    return listElements

def erange(*args):
    list = []
    start = 0
    step = 1
    if len(args) == 0:
        print("No arguments were given, the function takes 1 to 3 arguments!")
        return list
    elif len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        print("More than 3 arguments were given, the function takes 1 to 3 arguments!")
        return list

    while start < stop:
        list.append(start)
        start = start + step

    return list
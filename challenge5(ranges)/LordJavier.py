def erange(num):
    lis = []
    while num > 0:
        lis.append(num)
        num-=1
    lis = lis[::-1]
    lis = lis[:-1]
    lis.insert(0,num)
    return lis


def numerate(list):
    counter = 0
    for item in list:
        print(item, counter)
        counter +=1
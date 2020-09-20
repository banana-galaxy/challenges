def solution(a) :
    num = list(range(a+1))
    z_list = []
    y_list = []
    for i in num :
        if i == 0 :
            pass
        elif i%2 == 0 :
            z = i*i
            z_list.append(z)
        else :
            y = i*i
            y_list.append(y)
    return sum(z_list)-sum(y_list)
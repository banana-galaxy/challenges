def solution(num:int):
    numofmonths={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}#number of months
    usermonths=[] #next months
    for i in numofmonths:
        if numofmonths[i]==num and not i==12:
            if numofmonths[i+1] not in usermonths:
                usermonths.append(i+1)
    usernumofmonths=[] #num of days in next months
    for i in usermonths:
        if numofmonths[i] not in usernumofmonths:
            usernumofmonths.append(numofmonths[i])
    return usernumofmonths
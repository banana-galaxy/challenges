def solution(unwanted, numlist):
    found = False
    num = numlist[0]
    trial_factor = int(math.floor(math.sqrt(num)))
    while not found:
        if trial_factor == 1:
            return "Error"
        if num % trial_factor == 0:
            found = True
        else:
            trial_factor -= 1
    index = 1
    while numlist[index - 1] == numlist[index]:
        index += 1
    if numlist[index] % trial_factor == 0:
        newlist = [num / trial_factor, trial_factor]
    else:
        newlist = [trial_factor, num / trial_factor]
    index = 1
    while index < len(numlist):
        newlist.append(numlist[index] / newlist[index])
        index += 1
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sortlist = list(set(newlist))
    sortlist.sort()
    newtext = ""
    for entry in newlist:
        newtext += alpha[sortlist.index(entry)]
    return newtext
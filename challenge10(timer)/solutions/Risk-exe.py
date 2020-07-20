# I didn't read the question fully when I started
# so behold the spaghetti you're bearing witness to
# I had a couple of beers too.

def lateride(mins):
    h = 0
    h2 = 0 # cannot think of a good name for this variable

    for i in range(0, mins, 60):
        h += 1
        h2 = i

    moment = mins - h2

    if moment == 60:
        moment = 0
        h += 1

    if h < 10:
        h = "0" + str(h - 1)
    else:
        h = str(h - 1)

    if moment < 10:
        moment = "0" + str(moment)
    else:
        moment = str(moment)

    string = (str(h) + str(moment))
    ans = 0
    for i in range(0, len(string)):
        ans += int(string[i])

    return ans
def whichExit(matrix=None):
    if matrix == None:
        raise TypeError("You forgot to supply a 2d matrix")
    zidx = None #Prepping the zero index variable
    for m in matrix: #Getting the list from the matrix
        if 0 in m: #If there is a 0 in the list then grab it's position
            zidx = m.index(0)
    if zidx == None: #If there isn't one, then raise an error
        raise ValueError("There are no 0's (zero's) found in this matrix")
    elif zidx == 0 or sum(m[:zidx]) < sum(m[1+zidx:]): #If the 0 is in the first position, or the sum of the numbers to the Left are less than the ones on the right, then say "Left"
        return "Left"
    elif zidx == len(m)-1 or sum(m[:zidx]) > sum(m[1+zidx:]): #Same as above, only if the zero is in the last position, or the sum of the numbers to the right is less, then say "right"
        return "Right"
    else: #Otherwise say "Same"
        return "Same"
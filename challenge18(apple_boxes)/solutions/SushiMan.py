def appleBoxes(k: int):
    # sorry if i got this one wrong, I'm kind of a dumbass and have never tried this stuff

    yellow = ((1 / 5) * k) + (((3 / 5) * k) ** 2) + (k ** 2)
    red = (((2 / 5) * k) ** 2) + (((4 / 5) * k) ** 2)

    output = round(red - yellow)

    return output
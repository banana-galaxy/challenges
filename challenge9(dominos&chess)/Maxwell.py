def fill(checkboard):
    ones = []
    for row in checkboard:
        # get the position of every filled spot in the board
        ones += [i for i, value in enumerate(row) if value == 1]
    if sum(ones) % 2 == 0 and (len(checkboard) * len(checkboard[0]) - len(ones)) % 2 == 0:
        # If the sum of the positions of the filled spots is even
        # and if the number of empty spots is even
        return True
    return False
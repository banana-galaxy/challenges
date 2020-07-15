def fill(table):
    rows = 0
    for i in table:
        rows += 1
        columns = len(i)

    print(rows)
    print(columns)

    if rows == columns:
        return False
    else:
        if rows % 2 == 0 and columns % 2 == 1:
            return True
        elif rows % 2 == 1 and columns % 2 == 0:
            return True
        else:
            return False
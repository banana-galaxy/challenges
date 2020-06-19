def validate(postalCode):
    postal = str(postalCode)
    code = [postal[0]]
    for i, c in enumerate(postal[1:]):
        if c != postal[i]:
            continue
        else:
            return False

    if len(postal) == 5:
            return True
    else:
        return False
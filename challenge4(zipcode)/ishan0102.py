def validate(zip):
    # check if integer
    if not isinstance(zip, int):
        return False

    # check if len 5
    zip = str(zip)
    if len(zip) != 5:
        return False

    # check for alternating repetitive digits
    for i in range(3):
        if zip[i] == zip[i + 2]:
            return False

    # valid
    return True
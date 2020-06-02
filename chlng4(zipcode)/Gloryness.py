def validate(zip):
    # must be an int
    if not isinstance(zip, int):
        return False
    zipcode = str(zip)
    # loop through each num and count how many times num is shown in zip
    for index, num in enumerate(zipcode):
        # if appears more than once, then return False
        if zipcode.count(num) > 1:
            return False
    # check length, otherwise return True
    if len(zipcode) != 5:
        return False
    else:
        return True
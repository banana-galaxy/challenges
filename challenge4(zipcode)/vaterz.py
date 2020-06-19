def validate(x):
    """
    Validates a integer based zip code.
    Requirements:
        11xxx # two or more same digits in a row, not valid
        1x1xx # two or more neighboring digits, not valid
        1xx1x # no neighboring or next to each other digits, valid

    Parameters:
    x (int): the zipcode to validate.

    Returns:
        Boolean: True or False based on the requirements for valid Zip Code. 
    """
    numbers = "1234567890"
    x = str(x)
    s = len(x)
    z = 0

    # Checking size of Zip submitted
    if s == 5:
        for i in range(s):
            z = i + 1
            # Assuring that it's numbers being validated and that z is not throwing an index error
            if x[i] in numbers and z < s:
                # Checking for repetition
                if x[i] == x[z]:
                    return False
                # Making sure z does cause an index error
                if z + 1 < s:
                    # Checking for Neighboring numbers
                    if x[i] == x[z + 1]:
                        return False
            else:
                return False
    else:
        return False

    return True
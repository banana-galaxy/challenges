def validate(zip_code) -> bool:
    """Checks that a given zip code is valid or not.


    Function for the weekly challenge on Tech With Tim's discord server.
    
    Posted by Alex-Galaxy on 01/06/2020 in #challenge

    Task: Check that a given postal code is valid.

    The validation rules are:

        - it's made of only integers
        - there are 5 integers total, no less no more
        - there are no repetitive or neighboring digits

    That last check can be a bit confusing at first so let me try to explain it here:

    Let's say that x can be any digit

        - 11xxx isn't valid
        - 1x1xx isn't valid
        - 1xx1x is valid
    
    The grading criterias are:

        - No libraries/imports allowed
        - The code needs to be within a function
        - Have the function named exactly `validate`
        - Have the function take the code as an argument
        - Have the function return True if the code is valid, and False otherwise (do not throw exceptions or print stuff if it's not valid, just return False)
        - Obviously do all the checks
    
    Note:

        -I know this does not reflect how real world postal codes work. It was just a convenient naming for the challenge, any alternative challenge names are welcome.
        -You can only submit your code once, so check, double check, and triple check your solution before posting

    
    :param zip_code: zip code that needs to be validated
    :type zip_code: str | int

    :returns: the validation of the zip code
    :rtype: bool
    """

    zip_code = str(zip_code).zfill(5)
    if len(zip_code) != 5: return False
    if not zip_code.isdigit(): return False
    for i, c in enumerate(zip_code):
        if i >= 1 and zip_code[i-1] == c: return False
        if i >= 2 and zip_code[i-2] == c: return False
    return True

if __name__ == "__main__":
    print(validate(23456))
    print(validate(23556))
    print(validate(25456))
    print(validate("23r56"))
    print(validate(23453456))
    print(validate(236))
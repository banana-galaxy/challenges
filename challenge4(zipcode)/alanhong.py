def validate(code):
    checker = True
    if code.isdigit() and len(code) == 5:
        try:
            for index, num in enumerate(code):
                if num == code[index+1]:
                    checker = False
                elif num == code[index+2]:
                    checker = False
        finally:
            return checker
    else:
        return False
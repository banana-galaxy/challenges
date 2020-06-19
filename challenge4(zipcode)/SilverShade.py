def validate(code):
    digits = []
    for char in str(code):
        digits.append(int(char))
    for d in digits:
        if digits.count(d) > 1 and digits.index(d, (digits.index(d) + 1)) < (digits.index(d) + 3):
            valid = False
            break
        else:
            pass
        valid = True
    return valid
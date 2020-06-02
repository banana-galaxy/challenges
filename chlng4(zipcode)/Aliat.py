def validate(code):
    code = str(code)
    if len(code) != 5:
        return False
    for i in range(5):
        if code[i] < "0" or code[i] > "9":
            return False
        if i != 0 and code[i] == code[i - 1]:
            return False
        if i != 0 and i != 4 and code[i - 1] == code[i + 1]:
            return False
    return True
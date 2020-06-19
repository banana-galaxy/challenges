def validate(code):
    code = str(code)
    if not code.isdigit() or len(code) != 5:
        return False
    else:
        for i in range(len(code)):
            for j in range(i+1, len(code)):
                if code[i] == code[j] and abs(i-j) <= 2:
                    return False
        return True
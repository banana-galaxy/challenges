def validate(code):
    code = str(code)

    if len(code) == 5 and code.isdigit():
        for index, char in enumerate(code):
            try:
                if char == code[index+1]:
                    return False
                elif char == code[index+2]:
                    return False
            except IndexError:
                pass
        return True
    return False


if __name__ == "__main__":
    print(validate("56979"))
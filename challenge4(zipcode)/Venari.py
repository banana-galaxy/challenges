def validate(code):
    return all([len(set(str(code)[i:i+3])) == len(str(code)[i:i+3]) for i in range(3)]) and len(str(code)) == 5
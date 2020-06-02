def validate(codeP):
    try:
        int(codeP)
        if int(codeP/100000) == 0:
            code = str(codeP)
            for i in range(4):
                if code[i] != code[i+1]:
                    pass
                else: 
                    return False
                    quit()
            for i in range(1, 3):
                if code[i] != code[i+2]:
                    pass
                else: 
                    return False
                    quit()
            return True
        else:
            return False
    except:
        return False
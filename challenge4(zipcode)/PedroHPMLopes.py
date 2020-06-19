def validate(code):
    if type(code)==int: 
        code_list = list(str(code))
        if len(code_list) == 5:
            for i in range(1,4):
                x = code_list[i]
                if x == code_list[i+1] or x == code_list[i-1] or code_list[i-1] == code_list[i+1]:
                    result = False
                    break
                else: 
                    result = True
            return result
        else: 
            return False
    else: 
        return False
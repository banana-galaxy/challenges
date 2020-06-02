def validate(zip_code):
    try:
        if len(str(zip_code)) != 5:
            return False

        zip_code = list(str(int(zip_code)))

        for num in range(4):
            if num != 3:
                if zip_code[num] == zip_code[num+2]:
                    return False
            if zip_code[num] == zip_code[num+1]:
                return False
    except:
        return False
  
    return True
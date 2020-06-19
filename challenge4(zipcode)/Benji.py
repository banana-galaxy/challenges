def validate(postal):
    if postal in range(10000, 100000):
        bo = True
    else:
        bo = False
    if bo:
        postal_str = str(postal)
        list = []
        for i in range(5):
            list.append(postal_str[i:i+1])
        try:
            postal_int = int(postal_str)
            bo = True
        except:
            bo = False
        if bo:
            if list[0] == list[1] or list[1] == list[2] or list[2] == list[3] or list[3] == list[4] or list[0] == list[2] or list[1] == list[3] or list[2] == list[4]:
                return False
            else:
                return True
        else:
            return bo
    else:
        return bo
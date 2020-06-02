def validate(zipc):
    zipcode = str(zipc)
    prev = ""    
    if len(zipcode) == 5 and zipcode.isnumeric():
        list1 = []
        list2 = []
        for i in range(len(zipcode)):        
            if i % 2 == 0:
                if zipcode[i] not in list1 and zipcode[i] != prev and i < 4:
                    prev = zipcode[i]
                    list1.append(zipcode[i])
                elif i == 4:
                    if zipcode[i] == list1[1]:
                        return False
                    elif (zipcode[i] != list1[0] or zipcode[i] == list1[0]):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                if zipcode[i] not in list2 and zipcode[i] != prev:
                    prev = zipcode[i]
                    list2.append(zipcode[i])
                else:
                    return False
        return True
    else:
        return False
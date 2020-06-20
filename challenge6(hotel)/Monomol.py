def dicCreator(matrix):
    dic = {}
    # Cycles through matrix, where idx is index and l is each list
    for idx, l in enumerate(matrix):
        dic.update(fromListToDic(idx, l))
    return dic


def fromListToDic(index, l):
    # Transfers each list into dictionary, where k is its position and v is value
    dic = {}
    for idx, elem in enumerate(l):
        dic[f"R{index+1}C{idx+1}"] = elem
    return dic


def matrixSum(matrix):
    dic = dicCreator(matrix)
    sum = 0
    # print(dic)
    for idx, k in enumerate(dic):
        # First row, where numbers are always added up
        if k[1] == "1":
            sum += dic[k]
        else:
            # If the value is 0 then change value of key in R+1 (under this one) to None
            if dic[k] == 0:
                # dic[k] example R1C1 — if RxC1 in dic, where x is original value + 1
                if f"{k[0] + str(int(k[1]) + 1) + k[2:]}" in dic:
                    dic[f"{k[0] + str(int(k[1]) + 1) + k[2:]}"] = None
            if dic[k] is not None:
                sum += dic[k]
    return sum
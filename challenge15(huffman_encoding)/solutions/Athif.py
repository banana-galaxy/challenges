def solution():
    str = input("Enter your string : ")
    li = str.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i] = 3
        d[i] = d[i] - 1


print(d)

solution()
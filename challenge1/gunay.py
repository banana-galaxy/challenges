def solution(example,mult = -1):
    if mult == -1:
        mult = 64//len(example)
    for row in example:
        for i in range(1,(mult)*len(row),mult):
            for j in range(mult-1):
                row.insert(i, row[i-1])
    
    x = len(example)
    
    for c in range(1,mult*x,mult):
        for j in range(mult-1):    
            example.insert(c,example[c-1])
    return example
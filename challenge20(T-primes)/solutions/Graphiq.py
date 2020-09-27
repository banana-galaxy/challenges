def solution(n: int):
    var_1 = []
    for i in range(1, n+1):
        var_2 = n%i
        if var_2 == 0:
           var_1.insert(len(var_1), i)
    if len(var_1) == 3:
        return True
    else:
        return False
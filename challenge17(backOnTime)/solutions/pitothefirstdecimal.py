def solution(list):
    print(f' your route is: {list}')
    result_len = any(len(elem) >= 2 for elem in list)

    if len(list) > 10:
        return False

    else:
        if result_len == False:
            w = [s for s in list if s == 'w']
            e = [s for s in list if s == 'e']
            n = [s for s in list if s == 'n']
            s = [s for s in list if s == 's']
            sum = w + e + n + s

            if len(sum) == len(list):
                if len(w) == len(e):
                    if len(s) == len(n):
                        return True
                    else:
                        return False
                else:
                    return False
            elif len(sum) != len(list):
                return False
            else:
                return False
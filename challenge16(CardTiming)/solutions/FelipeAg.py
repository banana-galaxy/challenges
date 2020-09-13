def solution(s):
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    ans = []
    if s == 30:
        for month in months_30:
            if month + 1 == 2 and 28 not in ans:
                ans += [28]
            elif month + 1 in months_30 and 30 not in ans:
                ans += [30]
            elif month + 1 in months_31 and 31 not in ans:
                ans += [31]
    elif s == 31:
        for month in months_31:
            if month + 1 == 2 and 28 not in ans:
                ans += [28]
            elif month + 1 in months_30 and 30 not in ans:
                ans += [30]
            elif month + 1 in months_31 and 31 not in ans:
                ans += [31]
    else:
        ans += [31]
    return ans
def solution(lst):
    if len(lst) > 10:
        return False
    else:
        if lst.count("s") == lst.count("n") and lst.count("w") == lst.count("e"):
            return True
        else:
            return False
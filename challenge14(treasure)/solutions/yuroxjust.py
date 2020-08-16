def solution(value1, weight1, value2, weight2, maxw):
    best_score = 0
    try:
        if int(weight1) + int(weight2) <= int(maxw):
            best_score = int(value1) + int(value2)
        if int(weight1) <= int(maxw):
            score = int(value1)
            if score > best_score:
                best_score = score
        if int(weight2) <= int(maxw):
            score = int(value2)
            if score > best_score:
                best_score = score
    except ValueError:
        print("Please input only integers")
    return best_score
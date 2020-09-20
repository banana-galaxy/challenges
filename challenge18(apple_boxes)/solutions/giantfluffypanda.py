def solution(k):
    red_apples = 0
    yellow_apples = 0

    boxes = list(range(1, k+1))

    for box in boxes:
        if (box%2) == 0:
           apples = box * box
           red_apples += apples
        else:
            apples = box * box
            yellow_apples += apples

    dif = red_apples - yellow_apples

    return dif
def solution(k):
    yellow_apples, red_apples, apple_boxes = 0, 0, 0
    for x in range(k + 1):
        apples = x * x
        if apples % 2 == 0:
            red_apples = red_apples + apples
        else:
            yellow_apples = yellow_apples + apples
    apple_boxes = red_apples - yellow_apples
    return apple_boxes
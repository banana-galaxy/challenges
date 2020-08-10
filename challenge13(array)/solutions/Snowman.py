def solution(list):
    added_amount = 0
    for number in range(len(list) - 1):
        if list[number] >= list[number + 1]:
            added_amount += list[number] - list[number + 1] + 1
            list[number + 1] = list[number + 1] + list[number] - list[number + 1] + 1
    return added_amount, list
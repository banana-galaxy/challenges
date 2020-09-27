def solution(number):
    i = 1
    lists = []
    while i <= number:
        if (number % i == 0):
            lists.append(i)
        i = i + 1
    if len(lists) == 3:
        return True
    else:
        return False
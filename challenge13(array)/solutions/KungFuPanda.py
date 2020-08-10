def solution(array: list):
    moves = 0
    for index in range(len(array)):
        if index != len(array) - 1:
            while not array[index] < array[index + 1]:
                array[index + 1] += 1
                moves += 1

    return moves
def solution(int_array: list) -> int:
    moves: int = 0
    for i in range(len(int_array)-1):
        if int_array[i] >= int_array[i+1]:
            difference: int = int_array[i] - int_array[i+1]
            moves += difference + 1
    return moves
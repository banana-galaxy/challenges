def solution(number: int):
    List = [i for i in range(1, number+1) if number%i == 0]
    if len(List) == 3:
        return True
    else:
        return False 
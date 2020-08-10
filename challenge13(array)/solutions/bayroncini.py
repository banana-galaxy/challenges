def solution(list_of_numbers):
    result = 0
    ammount_of_numbers = len(list_of_numbers)

    for i in range(ammount_of_numbers):

        if i < ammount_of_numbers - 1:

            if list_of_numbers[i] >= list_of_numbers[i + 1]:
                difference = list_of_numbers[i] - list_of_numbers[i + 1] + 1
                result += difference
                list_of_numbers[i + 1] += difference

    return result
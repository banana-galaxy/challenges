def solution(inputArray):
    sol_counter = 0
    for n in range(0, len(inputArray) - 1):
        if inputArray[n] < inputArray[n + 1]:
            pass
        elif inputArray[n] == inputArray[n + 1]:
            inputArray[n + 1] += 1
            sol_counter += 1
        else:
            before = inputArray[n + 1]
            inputArray[n + 1] = inputArray[n] + 1
            after = inputArray[n + 1]
            sol_counter += after - before
    return sol_counter
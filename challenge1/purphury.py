def solution(input, output_size = 64):
    # input and output size will always be 2 to the power of 0 to 6 ({1,2,4,8,16,32,64})
    input_size = len(input[0])
    multiplier = output_size // input_size
    output = list()

    new_row = list()
    for row in input:
        new_row = list()
        for element in row:
            for i in range(multiplier):
                new_row.append(element)
        for i in range(multiplier):
            output.append(new_row)
    
    return output
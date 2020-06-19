def solution(input_image):
    output_image = [[None for _ in range(64)] for _ in range(64)]
    scale = 64 // len(input_image)
    for yPos in range(len(input_image)):
        for xPos in range(len(input_image[yPos])):
            for currentYpos in range(scale):
                for currentXpos in range(scale):
                    output_image[currentYpos + (scale * yPos)][currentXpos + (scale * xPos)] = input_image[yPos][xPos]
    return output_image
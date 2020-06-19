def solution(img, factor=64):
        result = [[0 for x in range(len(img)*factor)] for i in range(len(img)*factor)]

        for i in range(len(img)):
                for j in range(len(img)):
                        for a in range(factor):
                                for b in range(factor):
                                        result[(i * factor) + a][(j * factor)+ b] = img[i][j]

        return result
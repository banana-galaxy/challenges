def solution(img):
    new_image = []
    size = len(img[0])
    scale = int(64 / size)
    for line in img:
        new_image.insert(0, [])
        for i in line:
            for x in range(scale):
                new_image[0].append(i)
    new_image.sort()
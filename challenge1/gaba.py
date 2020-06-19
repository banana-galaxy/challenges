def solution(img):
    size=64
    shape = [len(img[0]), len(img)]
    if shape[0] != shape[1]:
        print("Please enter a square image")
        return
    dim = shape[0]
    if size < dim:
        print("Please enter a size greater than the original image")
        return
    new_image = []
    growth_factor = int(size / dim)
    for row in img:
        new_row = []
        for pix in row:
            for _ in range(growth_factor):
                new_row.append(pix)
        for _ in range(growth_factor):
            new_image.append(new_row)
    return new_image
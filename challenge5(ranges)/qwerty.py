def erange(*num):
    if len(num) > 3:
        raise TypeError(f"range expected at most 3 arguments, got {len(num)}")
    if len(num) == 1:
        num = (0, num[0])
    if len(num) == 2:
        num = (num[0], num[1], 1)
    step = num[2]
    i = num[0]
    while i < num[1]:
        yield i
        i += step

def numerate(nums, start=0):
    for i in nums:
        yield (start, i)
        start += 1
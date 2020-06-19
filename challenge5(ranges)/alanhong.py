def erange(*nums: int):
    start = nums[0]
    range_list = []
    for i in nums:
        if i is not int:
            raise TypeError(f"{type(i)} cannot be interpreted as an integer")
        
    if len(nums) == 3:
        if nums[2] >= 1 and nums[0] < nums[1]:
            while start < nums[1]:
                range_list.append(start)
                start += 1
            return range_list[::nums[2]]
        
        elif nums[0] > nums[1] and nums[2] < 0:
            while nums[1] < start:
                range_list.append(start)
                start -= 1
            return range_list[::abs(nums[2])]
        
        elif nums[2] == 0:
            raise ValueError("erange() arg 3 must not be zero")

        elif nums[0] == nums[1]:
            return range_list

        elif (nums[2] < 0 and nums[0] < nums[1]) or (nums[2] > 0 and nums[0] > nums[1]):
            return range_list

    elif len(nums) == 2:
        while start < nums[1]:
            range_list.append(start)
            start += 1
        return range_list

    elif len(nums) == 1:
        start = 0
        while start < nums[0]:
            range_list.append(start)
            start += 1
        return range_list

    elif len(nums) > 3:
        raise TypeError(f"erange() expected at most 3 arguments, got {len(nums)}")

def numerate(iterable=None, start=0):
    if start != 0:
        for i in iterable:
            yield tuple((start,i))
            start += 1

    elif iterable is not None and start == 0:
        for i in iterable:
            yield tuple((start, i))
            start += 1

    elif iterable is None:
        raise ValueError("enumerate() missing required argument 'iterable' (pos 1)")
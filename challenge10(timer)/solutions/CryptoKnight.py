def lateRide(clock):
    return sum([int(nums) for nums in str(int(clock / 60))]) + sum([int(nums) for nums in str(clock % 60)])
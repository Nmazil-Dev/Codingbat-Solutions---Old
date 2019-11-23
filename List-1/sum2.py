def sum2(nums):
    if len(nums) < 2:
        new =  nums[0] + nums[1]
        return new
    elif len(nums) == 0:
        new =  0
        return new
    else:
        new =  nums[0] + nums[1]
        return new
sum2([1,2,3])
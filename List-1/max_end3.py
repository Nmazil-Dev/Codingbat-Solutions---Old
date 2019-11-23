def max_end3(nums):
    new = []
    if nums[0] >= nums[2]:
        new.append(nums[0])
        new.append(nums[0])
        new.append(nums[0])
    elif nums[0] <= nums[2]:
        new.append(nums[2])
        new.append(nums[2])
        new.append(nums[2])
    return(new)
max_end3([1,2,3])
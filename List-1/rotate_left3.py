def rotate_left3(nums):
    new = []
    if len(nums) == 3:
        new.append(nums[1])
        new.append(nums[2])
        new.append(nums[0])
        return new
rotate_left3([1,2,3])
def has22(nums):
    if 2 in nums:
        two = nums.index(2)
        check =  two + 1
        if check >= len(nums):
            return False
        elif nums[two+1] == 2:
            return True
        else:
            return False
    else:
        return False
    print (nums[two])
has22([1, 2, 2])
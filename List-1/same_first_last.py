def same_first_last(nums):
    length =  len(nums) -1
    if len(nums) >= 1 and nums[0] == nums[length]:
        return True
    else:
        return False

same_first_last([1,2,3])
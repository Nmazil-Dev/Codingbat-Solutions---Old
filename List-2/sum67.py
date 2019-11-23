def sum67(nums):
    total = 0
    if 6 in nums:
        start =  nums.index(6)
        end = nums.index(7) + 1
        del nums[start:end]
        if 6 in nums:
            start =  nums.index(6)
            end = nums.index(7) + 1
            del nums[start:end]
        for i in nums:
            total += i
        return total
    else:
        for i in nums:
            total += i
        return total


sum67([1, 2, 2, 6, 99, 99, 7])
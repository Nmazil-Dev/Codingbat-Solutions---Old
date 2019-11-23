def sum13(nums):
    total = 0
    if len(nums) == 0:
        return 0
    elif 13 in nums:
        place = nums.index(13)
        nums = nums[:place]
        for i in nums:
            total += i
        return total
    else:
        for i in nums:
            total += i 
        return total

sum13([1, 2, 2, 1])
def centered_average(nums):
    min_num = min(nums)
    max_num = max(nums)
    nums.remove(max_num)
    nums.remove(min_num)
    total = 0
    for i in nums:
        total += i

    return total / len(nums)



centered_average([1, 2, 3, 4, 100])
  
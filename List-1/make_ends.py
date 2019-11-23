def make_ends(nums):
    new_list = []
    end = len(nums) -1
    new_list.append(nums[0])
    new_list.append(nums[end])
    return new_list

make_ends([1,2,3])
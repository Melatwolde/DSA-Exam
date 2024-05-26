def target_find(nums, target):
    l , r = 0 , len(nums)-1
    nums.sort()
    while l < r:
        if nums[l] + nums[r] > target:
            r -=1
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            return [l,r]
nums = [2,7,11,15]
target = 9
print(target_find(nums, target))

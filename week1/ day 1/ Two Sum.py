def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        current = nums[i]
        required = target - current
        if required in seen:
            return [seen[required], i]
        seen[current] = i
    return []
nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))


# Time Complexity: O(n)
# Space Complexity: O(n)
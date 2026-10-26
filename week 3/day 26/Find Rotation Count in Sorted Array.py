def rotation_count(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return low

print(rotation_count([4, 5, 6, 7, 1, 2, 3]))
print(rotation_count([3, 4, 5, 1, 2]))
print(rotation_count([1, 2, 3, 4, 5]))
print(rotation_count([2, 1]))



# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_minimum(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]

print(find_minimum([3, 4, 5, 1, 2]))
print(find_minimum([4, 5, 6, 7, 0, 1, 2]))
print(find_minimum([11, 13, 15, 17]))


# Time Complexity: O(log n)
# Space Complexity: O(1)
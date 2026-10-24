def countOccurrences(nums, target):
    first = -1
    last = -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            first = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if first == -1:
        return 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            last = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last - first + 1

nums = [1, 2, 2, 2, 3, 4, 5]
target = 2

print(countOccurrences(nums, target))


# Time Complexity: O(log n)
# Auxiliary Space: O(1)

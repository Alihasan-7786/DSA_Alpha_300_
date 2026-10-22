def search_insert(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

nums = [1, 3, 5, 6]
target = 2

print(search_insert(nums, target))



# Time Complexity: O(log n)
# Space Complexity: O(1)

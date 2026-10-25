def find_peak_element(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low

print(find_peak_element([1, 2, 3, 1]))
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))


# Time Complexity: O(log n)
# Space Complexity: O(1)

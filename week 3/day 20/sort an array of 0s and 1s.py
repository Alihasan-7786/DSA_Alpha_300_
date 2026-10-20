def sort_binary(nums):
    zeros = 0
    for num in nums:
        if num == 0:
            zeros += 1
    for i in range(len(nums)):
        if i < zeros:
            nums[i] = 0
        else:
            nums[i] = 1
    return nums


nums = [1, 0, 1, 1, 0, 0, 1]
print("Sorted array:", sort_binary(nums))


# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# Pattern: Counting

def sort_array_by_parity(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] % 2 == 1 and nums[j + 1] % 2 == 0:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums
nums = [3, 1, 2, 4]
print(sort_array_by_parity(nums))
# Time Complexity: O(n^2)
# Space Complexity: O(1)

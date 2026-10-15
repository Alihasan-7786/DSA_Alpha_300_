def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums
nums = [5, 2, 8, 1, 3]
print(bubble_sort(nums))
# Time Complexity: O(n^2)
# Space Complexity: O(1)

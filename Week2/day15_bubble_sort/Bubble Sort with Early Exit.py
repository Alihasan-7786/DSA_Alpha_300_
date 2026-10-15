def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                swapped = True
        if swapped == False:
            break
    return nums
nums = [1, 2, 3, 4, 5]
print(bubble_sort(nums))
# Worst Time: O(n^2)
# Best Time: O(n)
# Space Complexity: O(1)

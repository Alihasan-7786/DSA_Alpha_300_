# Method 1: Counting Sort
def counting_sort(nums):
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1
    index = 0
    for num in range(3):
        while count[num] > 0:
            nums[index] = num
            index += 1
            count[num] -= 1
    return nums
nums = [2, 0, 2, 1, 1, 0]
print("Counting Sort:", counting_sort(nums))

# Method 2: Dutch National Flag
def dutch_flag(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
nums = [2, 0, 2, 1, 1, 0]
print("Dutch National Flag:", dutch_flag(nums))

# Both methods:
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)

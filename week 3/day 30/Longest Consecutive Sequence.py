def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
def longest_consecutive(nums):
    if len(nums) == 0:
        return 0
    nums = merge_sort(nums)
    longest = 1
    current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        if nums[i] == nums[i - 1] + 1:
            current += 1
        else:
            current = 1
        if current > longest:
            longest = current
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longest_consecutive([1, 2, 0, 1]))
print(longest_consecutive([]))


# Time Complexity: O(n * log(n))
# Space Complexity: O(n)

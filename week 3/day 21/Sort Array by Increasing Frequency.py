def frequency_sort(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = nums[j]
            b = nums[j + 1]
            if freq[a] > freq[b] or (freq[a] == freq[b] and a < b):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

arr = [1, 1, 2, 2, 2, 3]
print(frequency_sort(arr))


# Time Complexity: O(n^2)
# Space Complexity: O(n)
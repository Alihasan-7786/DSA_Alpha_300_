def wiggle_sort(nums):
    i = 0
    while i < len(nums) - 1:
        if i % 2 == 0:
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        i += 1
    return nums

arr = [3, 5, 2, 1, 6, 4]
print(wiggle_sort(arr))

#time complexity : O(n)
#space complexity: O(1)
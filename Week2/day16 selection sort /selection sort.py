def selection_sort(nums):
  n = len(nums)
  for i in range(n):
    small = i
    for j in range(i + 1, n):
      if nums[j] < nums[small]:
        small = j
    temp = nums[i]
    nums[i] = nums[small]
    nums[small] = temp
  return nums
nums = [64, 25, 12, 11, 18]
print(selection_sort(nums))
# time complexity : o(n^2)
# space complexity : o(1)

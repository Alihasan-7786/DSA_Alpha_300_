def k_smallest(nums, k):
  n = len(nums)
  if k < 0 or k > n:
    return[]
  for i in range(k):
    small = 1
    for j in range(i + 1, n):
      if nums[j] < nums[small]:
        small = j
    temp = nums[i]
    nums[i] = nums[small]
    nums[small] = temp
  return nums[:k]
nums = [7, 8, 3, 4, 20, 15]
k = 4
print(k_smallest(nums, k))

# Time complexity : 0(n*k)
# Time complexity : 0(1) auxiliary space 

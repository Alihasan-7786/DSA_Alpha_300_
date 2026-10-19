def quick_sort(nums):
  if len(nums) <= 1:
    return nums
  pivot = nums[-1]
  low = []
  high = []
  for i in range(len(nums) - 1):
    if nums[i] < pivot:
      low.append(num[i])
    else:
      high.append(nums[i])
  return quick_sort(low) + [pivot] + quick+sort(high)
size = int(input("Enter rray size:")
values = []
for i in range(size):
  x = int(input("Enter value: "))
  values.append(x)
print("Given array:", values)
answer = quick_sort(values)
print("Sorted array:", answer)

# Time Complexity:
# Average: O(n log n)
# Worst: O(n^2)

# Space Complexity: O(n) auxiliary list space,
# excluding recursion stack

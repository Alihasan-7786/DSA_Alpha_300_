def findFloor(nums, x):
    left = 0
    right = len(nums) - 1
    floor = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= x:
            floor = nums[mid]
            left = mid + 1
        else:
            right = mid - 1
    return floor

def findCeiling(nums, x):
    left = 0
    right = len(nums) - 1
    ceiling = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= x:
            ceiling = nums[mid]
            right = mid - 1
        else:
            left = mid + 1
    return ceiling

nums = [1, 2, 4, 6, 10]
x = 5

print("Floor =", findFloor(nums, x))
print("Ceiling =", findCeiling(nums, x))



# Time Complexity: O(log n)
# Auxiliary Space: O(1)

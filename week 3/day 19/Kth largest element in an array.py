
class Solution(object):
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        def quickselect(left, right):
            pivot = nums[right]
            p = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]
            if p == target:
                return nums[p]
            elif p < target:
                return quickselect(p + 1, right)
            else:
                return quickselect(left, p - 1)
        return quickselect(0, len(nums) - 1)
      
# Average Time Complexity: O(n)
# Worst-case Time Complexity: O(n^2)
# Auxiliary Space Complexity: O(n) worst case due to recursion

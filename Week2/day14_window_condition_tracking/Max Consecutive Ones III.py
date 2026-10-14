class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        maxlength = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            length = right - left + 1
            if length > maxlength:
                maxlength = length
        return maxlength
nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
k = 2
obj = Solution()
print(obj.longestOnes(nums, k))
# Time Complexity: O(n)
# Space Complexity: O(1)

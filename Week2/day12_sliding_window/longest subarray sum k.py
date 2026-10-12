class Solution:
    def longestSubarray(self, nums, k):
        left = 0
        total = 0
        result = 0
        for right in range(len(nums)):
            total += nums[right]
            while total > k and left <= right:
                total -= nums[left]
                left += 1
            if total == k:
                length = right - left + 1
                if length > result:
                    result = length
        return result
nums = [1, 2, 1, 1, 1]
k = 3
obj = Solution()
print(obj.longestSubarray(nums, k))


class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        ans = len(nums) + 1
        for right in range(len(nums)):
            total = total + nums[right]
            while total >= target:
                length = right - left + 1
                if length < ans:
                    ans = length
                total = total - nums[left]
                left = left + 1
        if ans == len(nums) + 1:
            return 0
        return ans
nums = [2, 3, 1, 2, 4, 3]
target = 7
obj = Solution()
print(obj.minSubArrayLen(target, nums))

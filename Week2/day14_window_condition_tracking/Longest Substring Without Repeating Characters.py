class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        maxlength = 0
        last_seen = {}
        for right in range(len(s)):
            ch = s[right]
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            length = right - left + 1
            if length > maxlength:
                maxlength = length
        return maxlength
s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))
# Time Complexity: O(n)
# Space Complexity: O(min(n, a))

class Solution:
    def characterReplacement(self, s, k):
        left = 0
        maxfreq = 0
        maxlength = 0
        count = {}
        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1
            if count[ch] > maxfreq:
                maxfreq = count[ch]
            while (right - left + 1) - maxfreq > k:
                old = s[left]
                count[old] -= 1
                left += 1
            length = right - left + 1
            if length > maxlength:
                maxlength = length
        return maxlength
s = "AABABBA"
k = 1
obj = Solution()
print(obj.characterReplacement(s, k))
# Time Complexity: O(n)
# Space Complexity: O(1) for uppercase English letters

class Solution:
    def findAnagrams(self, s, p):
        result = []
        n = len(s)
        m = len(p)
        if m > n:
            return result
        p_count = {}
        window = {}
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1
        for i in range(m):
            ch = s[i]
            window[ch] = window.get(ch, 0) + 1
        if window == p_count:
            result.append(0)
        for right in range(m, n):
            new_char = s[right]
            window[new_char] = window.get(new_char, 0) + 1
            old_char = s[right - m]
            window[old_char] -= 1
            if window[old_char] == 0:
                del window[old_char]
            if window == p_count:
                result.append(right - m + 1)
        return result
s = "cbaebabacd"
p = "abc"
obj = Solution()
print(obj.findAnagrams(s, p))
# Time Complexity: O(n * a) worst case for dictionary comparisons
# Space Complexity: O(a)

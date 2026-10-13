class Solution:
    def checkInclusion(self, s1, s2):
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        count1 = {}
        window = {}
        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1
        for i in range(m):
            ch = s2[i]
            window[ch] = window.get(ch, 0) + 1
        if window == count1:
            return True
        for right in range(m, n):
            new_char = s2[right]
            window[new_char] = window.get(new_char, 0) + 1
            old_char = s2[right - m]
            window[old_char] -= 1
            if window[old_char] == 0:
                del window[old_char]
            if window == count1:
                return True
        return False
s1 = "ab"
s2 = "eidbaooo"
obj = Solution()
print(obj.checkInclusion(s1, s2))

# Time Complexity: O(n * a) worst case for dictionary comparisons
# Space Complexity: O(a)

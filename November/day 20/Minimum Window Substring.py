def min_window(s, t):
    if len(t) > len(s) or len(t) == 0:
        return ""
    need = {}
    window = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    required = len(need)
    matched = 0
    left = 0
    min_length = len(s) + 1
    start = 0
    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            matched += 1
        while matched == required:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                start = left
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                matched -= 1
            left += 1
    if min_length == len(s) + 1:
        return ""

    return s[start:start + min_length]

s = "ADOBECODEBANC"
t = "ABC"
result = min_window(s, t)
print(result)



# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
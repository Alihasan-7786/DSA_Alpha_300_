def find_anagrams(s, p):
    result = []
    if len(p) > len(s):
        return result
    p_count = {}
    window_count = {}
    for ch in p:
        if ch not in p_count:
            p_count[ch] = 0
        p_count[ch] += 1
    window_size = len(p)
    for i in range(window_size):
        ch = s[i]
        if ch not in window_count:
            window_count[ch] = 0
        window_count[ch] += 1
    if window_count == p_count:
        result.append(0)
    for right in range(window_size, len(s)):
        new_char = s[right]
        if new_char not in window_count:
            window_count[new_char] = 0
        window_count[new_char] += 1
        left_char = s[right - window_size]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        if window_count == p_count:
            result.append(right - window_size + 1)

    return result

s = "cbaebabacd"
p = "abc"
result = find_anagrams(s, p)
print(result)




# Time Complexity: O(n * k) in the worst case due to dictionary comparisons
# Space Complexity: O(k)
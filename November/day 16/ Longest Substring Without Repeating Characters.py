def longest_substring(s):
    char_index = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        current_char = s[right]
        if current_char in char_index and char_index[current_char] >= left:
            left = char_index[current_char] + 1
        char_index[current_char] = right
        window_length = right - left + 1
        if window_length > max_length:
            max_length = window_length
    return max_length

s = "abcabcbb"

result = longest_substring(s)
print(result)





# Time Complexity: O(n)
# Space Complexity: O(min(n, k))
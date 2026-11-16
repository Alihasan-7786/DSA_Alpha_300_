def character_replacement(s, k):
    char_count = {}
    left = 0
    max_frequency = 0
    max_length = 0
    for right in range(len(s)):
        current_char = s[right]
        if current_char not in char_count:
            char_count[current_char] = 0
        char_count[current_char] += 1
        if char_count[current_char] > max_frequency:
            max_frequency = char_count[current_char]
        window_length = right - left + 1
        if window_length - max_frequency > k:
            left_char = s[left]
            char_count[left_char] -= 1
            left += 1
        window_length = right - left + 1
        if window_length > max_length:
            max_length = window_length

    return max_length

s = "AABABBA"
k = 1
result = character_replacement(s, k)
print(result)





# Time Complexity: O(n)
# Space Complexity: O(1) - at most 26 uppercase letters
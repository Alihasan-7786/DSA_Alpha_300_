def reorganize_string(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    max_char = ""
    max_count = 0
    for ch in freq:
        if freq[ch] > max_count:
            max_char = ch
            max_count = freq[ch]
    if max_count > (len(s) + 1) // 2:
        return ""
    result = [""] * len(s)
    index = 0
    for ch in freq:
        count = freq[ch]
        for i in range(count):
            if index >= len(s):
                index = 1
            result[index] = ch
            index += 2
    return "".join(result)

s = "aab"

result = reorganize_string(s)
print(result)





# Time Complexity: O(n)
# Space Complexity: O(n)
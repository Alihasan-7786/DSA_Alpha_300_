def reorganize_string(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    chars = list(freq.keys())
    for i in range(1, len(chars)):
        current = chars[i]
        j = i - 1
        while j >= 0 and freq[chars[j]] < freq[current]:
            chars[j + 1] = chars[j]
            j -= 1
        chars[j + 1] = current
    if freq[chars[0]] > (len(s) + 1) // 2:
        return ""
    result = [""] * len(s)
    index = 0
    for ch in chars:
        for _ in range(freq[ch]):
            if index >= len(s):
                index = 1
            result[index] = ch
            index += 2
    return "".join(result)

s = "aab"
print(reorganize_string(s))




# Time Complexity: O(n + k²)
# Space Complexity: O(n + k)
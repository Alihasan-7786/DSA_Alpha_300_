def frequency_sort(s):
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
    result = []
    for ch in chars:
        for _ in range(freq[ch]):
            result.append(ch)
    return "".join(result)

s = "tree"
print(frequency_sort(s))



# Time Complexity: O(n + k²)
# Space Complexity: O(n + k)
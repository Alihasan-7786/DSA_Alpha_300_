def frequency_sort(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    chars = list(freq.keys())
    for i in range(len(chars)):
        max_index = i
        for j in range(i + 1, len(chars)):
            if freq[chars[j]] > freq[chars[max_index]]:
                max_index = j
        chars[i], chars[max_index] = chars[max_index], chars[i]
    result = []
    for ch in chars:
        result.append(ch * freq[ch])
    return "".join(result)

s = "tree"
result = frequency_sort(s)
print(result)




# Time Complexity: O(n + k^2)
# Space Complexity: O(n + k)
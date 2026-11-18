def custom_sort_string(order, s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    result = []
    for ch in order:
        if ch in freq:
            for i in range(freq[ch]):
                result.append(ch)
            del freq[ch]
    for ch in freq:
        for i in range(freq[ch]):
            result.append(ch)

    return "".join(result)

order = "cba"
s = "abcd"

result = custom_sort_string(order, s)
print(result)




# Time Complexity: O(n + m)
# Space Complexity: O(n + k)
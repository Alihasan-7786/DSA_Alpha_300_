def rearrange_characters(s, target):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    target_freq = {}
    for ch in target:
        if ch in target_freq:
            target_freq[ch] += 1
        else:
            target_freq[ch] = 1
    result = len(s)
    for ch in target_freq:
        if ch not in freq:
            return 0
        count = freq[ch] // target_freq[ch]
        if count < result:
            result = count
    return result

s = "ilovecodingonleetcode"
target = "code"
print(rearrange_characters(s, target))




# Time Complexity: O(n + m)
# Space Complexity: O(k)
def first_unique_char(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1


s = "alpha"

result = first_unique_char(s)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(k)

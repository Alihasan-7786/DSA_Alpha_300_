def longest_palindrome(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    length = 0
    odd_found = False
    for count in freq.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True
    if odd_found:
        length += 1

    return length

s = "abccccdd"
result = longest_palindrome(s)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(k)

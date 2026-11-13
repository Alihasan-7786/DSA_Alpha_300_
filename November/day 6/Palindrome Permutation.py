def can_permute_palindrome(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    odd_count = 0
    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1
    if odd_count <= 1:
        return True
    else:
        return False

s = "aab"
result = can_permute_palindrome(s)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(k)

def count_substrings(s):
    count = 0
    n = len(s)
    for i in range(n):
        left = i
        right = i
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count

s = "aaa"
result = count_substrings(s)
print(result)


# Time Complexity: O(n^2)
# Space Complexity: O(1)

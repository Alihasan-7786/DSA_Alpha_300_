def reverse_string(s, k):
    chars = list(s)
    n = len(chars)
    start = 0
    while start < n:
        left = start
        right = min(start + k - 1, n - 1)
        while left < right:
            temp = chars[left]
            chars[left] = chars[right]
            chars[right] = temp
            left += 1
            right -= 1
        start += 2 * k
    return "".join(chars)

s = "abcdefg"
k = 2

result = reverse_string(s, k)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(n)
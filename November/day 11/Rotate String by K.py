def rotate_string_by_k(s, k):
    n = len(s)
    if n == 0:
        return s
    k = k % n
    chars = list(s)
    result = []
    i = n - k
    while i < n:
        result.append(chars[i])
        i += 1
    i = 0
    while i < n - k:
        result.append(chars[i])
        i += 1
    return "".join(result)
s = "abcdefg"
k = 2
result = rotate_string_by_k(s, k)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(n)
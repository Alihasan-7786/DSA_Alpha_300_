def str_str(haystack, needle):
    n = len(haystack)
    m = len(needle)
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            return i

    return -1

haystack = "sadbutsad"
needle = "sad"
result = str_str(haystack, needle)
print(result)




# Time Complexity: O(n * m)
# Space Complexity: O(1)
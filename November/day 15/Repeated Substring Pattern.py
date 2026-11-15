def repeated_substring_pattern(s):
    n = len(s)
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            repeat_count = n // length
            match = True
            for i in range(n):
                if s[i] != s[i % length]:
                    match = False
                    break
            if match and repeat_count > 1:
                return True

    return False

s = "abab"
result = repeated_substring_pattern(s)
print(result)




# Time Complexity: O(n^2)
# Space Complexity: O(1)
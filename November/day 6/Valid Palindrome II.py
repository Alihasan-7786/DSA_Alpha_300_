def is_palindrome_range(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return (is_palindrome_range(s, left + 1, right) or
                    is_palindrome_range(s, left, right - 1))
        left += 1
        right -= 1

    return True

s = "abca"
result = valid_palindrome(s)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(1)

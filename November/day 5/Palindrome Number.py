def is_palindrome(x):
    if x < 0:
        return False
    original = x
    reverse = 0
    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10

    return original == reverse

x = 121
result = is_palindrome(x)
print(result)


# Time Complexity: O(log10(n))
# Space Complexity: O(1)

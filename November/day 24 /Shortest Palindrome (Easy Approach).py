def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def shortest_palindrome(s):
    end = len(s) - 1
    while end >= 0:
        if is_palindrome(s, 0, end):
            break
        end -= 1
    to_add = []
    for i in range(len(s) - 1, end, -1):
        to_add.append(s[i])
    prefix = "".join(to_add)
    return prefix + s

s = "aacecaaa"
result = shortest_palindrome(s)
print(result)





# Time Complexity: O(n²)
# Space Complexity: O(n)
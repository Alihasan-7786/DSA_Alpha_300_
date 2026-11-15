def reverse_only_letters(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1
    while left < right:
        if not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha():
            right -= 1
        else:
            temp = chars[left]
            chars[left] = chars[right]
            chars[right] = temp
            left += 1
            right -= 1
    return "".join(chars)

s = "a-bC-dEf-ghIj"
result = reverse_only_letters(s)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(n)
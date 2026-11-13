def to_lower_case(s):
    result = []
    for ch in s:
        if ch >= 'A' and ch <= 'Z':
            new_char = chr(ord(ch) + 32)
            result.append(new_char)
        else:
            result.append(ch)
    return "".join(result)

s = "Hello"

result = to_lower_case(s)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(n)

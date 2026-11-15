def reverse_prefix(word, ch):
    chars = list(word)
    position = -1
    for i in range(len(chars)):
        if chars[i] == ch:
            position = i
            break
    if position == -1:
        return word
    left = 0
    right = position
    while left < right:
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp
        left += 1
        right -= 1
    return "".join(chars)

word = "abcdefd"
ch = "d"

result = reverse_prefix(word, ch)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    characters = list(s)
    left = 0
    right = len(characters) - 1
    while left < right:
        while left < right and characters[left] not in vowels:
            left += 1
        while left < right and characters[right] not in vowels:
            right -= 1
        temp = characters[left]
        characters[left] = characters[right]
        characters[right] = temp
        left += 1
        right -= 1
    return "".join(characters)

s = "hello"
result = reverse_vowels(s)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(n)

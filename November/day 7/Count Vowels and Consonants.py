def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for ch in s:
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)
        if ch >= 'a' and ch <= 'z':
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

s = "Hello World"
vowels, consonants = count_vowels_consonants(s)
print("Vowels:", vowels)
print("Consonants:", consonants)


# Time Complexity: O(n)
# Space Complexity: O(1)
def count_vowel_substrings(word):
    vowels = "aeiou"
    total = 0
    for i in range(len(word)):
        vowel_count = {}
        for j in range(i, len(word)):
            ch = word[j]
            if ch not in vowels:
                break
            if ch not in vowel_count:
                vowel_count[ch] = 0
            vowel_count[ch] += 1
            if len(vowel_count) == 5:
                total += 1

    return total

word = "aeiouu"
result = count_vowel_substrings(word)
print(result)




# Time Complexity: O(n^2)
# Space Complexity: O(1) - at most 5 vowel entries
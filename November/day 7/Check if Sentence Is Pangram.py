def check_if_pangram(sentence):
    letters = [False] * 26
    for ch in sentence:
        index = ord(ch) - ord('a')
        letters[index] = True
    for i in range(26):
        if letters[i] == False:
            return False
    return True
sentence = "thequickbrownfoxjumpsoverthelazydog"
result = check_if_pangram(sentence)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(1)
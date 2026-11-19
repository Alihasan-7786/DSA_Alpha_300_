def find_longest_word(s, dictionary):
    best = ""
    for word in dictionary:
        i = 0
        j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1
        if j == len(word):
            if len(word) > len(best):
                best = word
            elif len(word) == len(best) and word < best:
                best = word

    return best

s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
result = find_longest_word(s, dictionary)
print(result)




# Time Complexity: O(n + D * (n + L))
# Space Complexity: O(1)
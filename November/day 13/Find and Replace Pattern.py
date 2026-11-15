def find_and_replace_pattern(words, pattern):
    result = []
    for word in words:
        if len(word) != len(pattern):
            continue
        pattern_to_word = {}
        word_to_pattern = {}
        match = True
        for i in range(len(pattern)):
            p = pattern[i]
            w = word[i]
            if p in pattern_to_word:
                if pattern_to_word[p] != w:
                    match = False
                    break
            else:
                pattern_to_word[p] = w
            if w in word_to_pattern:
                if word_to_pattern[w] != p:
                    match = False
                    break
            else:
                word_to_pattern[w] = p
        if match:
            result.append(word)
    return result

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
result = find_and_replace_pattern(words, pattern)
print(result)





# Time Complexity: O(w * n)
# Space Complexity: O(n)
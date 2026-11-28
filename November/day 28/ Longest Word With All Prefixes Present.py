def longest_word(words):
    word_set = set(words)
    result = ""
    for word in words:
        valid = True
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if prefix not in word_set:
                valid = False
                break
        if valid:
            if len(word) > len(result):
                result = word
            elif len(word) == len(result) and word < result:
                result = word
    return result

words = ["w", "wo", "wor", "worl", "world"]
print(longest_word(words))





# Time Complexity: O(n × L²)
# Space Complexity: O(n × L)
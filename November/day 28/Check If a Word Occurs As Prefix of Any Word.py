def is_prefix_of_word(sentence, search_word):
    words = sentence.split()
    for i in range(len(words)):
        word = words[i]
        if len(search_word) <= len(word):
            match = True
            for j in range(len(search_word)):
                if word[j] != search_word[j]:
                    match = False
                    break
            if match:
                return i + 1
    return -1

sentence = "i love eating burger"
search_word = "burg"
print(is_prefix_of_word(sentence, search_word))




# Time Complexity: O(n × L)
# Space Complexity: O(n × L)
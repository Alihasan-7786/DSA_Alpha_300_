def count_words(s):
    count = 0
    in_word = False
    for ch in s:
        if ch != " ":
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count

s = "Hello, how are you?"
result = count_words(s)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(1)
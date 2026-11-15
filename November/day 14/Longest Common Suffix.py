def longest_common_suffix(words):
    if len(words) == 0:
        return ""
    suffix = []
    first_word = words[0]
    for i in range(1, len(first_word) + 1):
        current_char = first_word[len(first_word) - i]
        for j in range(1, len(words)):
            if i > len(words[j]):
                return "".join(reversed(suffix))
            if words[j][len(words[j]) - i] != current_char:
                return "".join(reversed(suffix))
        suffix.append(current_char)
    return "".join(reversed(suffix))

words = ["running", "jogging", "walking"]

result = longest_common_suffix(words)
print(result)





# Time Complexity: O(n * m)
# Space Complexity: O(m)
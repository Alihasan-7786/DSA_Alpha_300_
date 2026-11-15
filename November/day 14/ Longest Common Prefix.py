def longest_common_prefix(words):
    if len(words) == 0:
        return ""
    prefix = []
    for i in range(len(words[0])):
        current_char = words[0][i]
        for j in range(1, len(words)):
            if i >= len(words[j]) or words[j][i] != current_char:
                return "".join(prefix)
        prefix.append(current_char)
    return "".join(prefix)

words = ["flower", "flow", "flight"]
result = longest_common_prefix(words)
print(result)





# Time Complexity: O(n * m)
# Space Complexity: O(m)
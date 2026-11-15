def reverse_words(s):
    words = []
    current = []
    for ch in s:
        if ch != " ":
            current.append(ch)
        else:
            if len(current) > 0:
                words.append("".join(current))
                current = []
    if len(current) > 0:
        words.append("".join(current))
    result = []
    i = len(words) - 1
    while i >= 0:
        result.append(words[i])
        i -= 1
    return " ".join(result)

s = "  the sky is blue  "
result = reverse_words(s)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(n)
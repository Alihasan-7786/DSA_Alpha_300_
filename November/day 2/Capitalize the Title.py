def capitalize_title(title):
    words = title.split()
    result = []
    for word in words:
        new_word = []
        for i in range(len(word)):
            ch = word[i]
            if len(word) <= 2:
                if ch >= 'A' and ch <= 'Z':
                    ch = chr(ord(ch) + 32)
            elif i == 0:
                if ch >= 'a' and ch <= 'z':
                    ch = chr(ord(ch) - 32)
            else:
                if ch >= 'A' and ch <= 'Z':
                    ch = chr(ord(ch) + 32)
            new_word.append(ch)
        result.append("".join(new_word))

    return " ".join(result)

title = "capiTalIze tHe titLe"

result = capitalize_title(title)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(n)

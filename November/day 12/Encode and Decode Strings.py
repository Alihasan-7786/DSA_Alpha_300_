def encode(words):
    result = []
    for word in words:
        result.append(str(len(word)))
        result.append("#")
        result.append(word)
    return "".join(result)

def decode(s):
    result = []
    i = 0
    while i < len(s):
        length = 0
        while s[i] != "#":
            length = length * 10 + int(s[i])
            i += 1
        i += 1
        word = s[i:i + length]
        result.append(word)
        i += length
    return result

words = ["hello", "world", "python"]
encoded = encode(words)
decoded = decode(encoded)
print(encoded)
print(decoded)




# Time Complexity: O(n)
# Space Complexity: O(n)
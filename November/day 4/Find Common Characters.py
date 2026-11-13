def common_chars(words):
    common = [0] * 26
    for ch in words[0]:
        index = ord(ch) - ord('a')
        common[index] += 1
    for word in words[1:]:
        current = [0] * 26
        for ch in word:
            index = ord(ch) - ord('a')
            current[index] += 1
        for i in range(26):
            if current[i] < common[i]:
                common[i] = current[i]
    result = []

    for i in range(26):
        for j in range(common[i]):
            result.append(chr(i + ord('a')))

    return result

words = ["bella", "label", "roller"]
result = common_chars(words)
print(result)


# Time Complexity: O(n * k + 26 * n)
# Space Complexity: O(26 + r)

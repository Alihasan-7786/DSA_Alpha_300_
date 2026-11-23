def close_strings(word1, word2):
    if len(word1) != len(word2):
        return False
    freq1 = {}
    freq2 = {}
    for ch in word1:
        freq1[ch] = freq1.get(ch, 0) + 1
    for ch in word2:
        freq2[ch] = freq2.get(ch, 0) + 1
    for ch in freq1:
        if ch not in freq2:
            return False
    for ch in freq2:
        if ch not in freq1:
            return False
    count1 = {}
    count2 = {}
    for value in freq1.values():
        count1[value] = count1.get(value, 0) + 1
    for value in freq2.values():
        count2[value] = count2.get(value, 0) + 1
    for value in count1:
        if count1[value] != count2.get(value, 0):
            return False
    for value in count2:
        if value not in count1:
            return False

    return True

word1 = "abc"
word2 = "bca"
result = close_strings(word1, word2)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(k)
def group_anagrams(strs):
    groups = {}
    for word in strs:
        count = [0] * 26
        for ch in word:
            index = ord(ch) - ord('a')
            count[index] += 1
        key = tuple(count)
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return list(groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = group_anagrams(strs)
print(result)


# Time Complexity: O(n * k)
# Space Complexity: O(n * k)

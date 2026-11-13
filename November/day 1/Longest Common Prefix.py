def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""
    prefix = []
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return "".join(prefix)
        prefix.append(char)
    return "".join(prefix)

strs = ["flower", "flow", "flight"]

result = longest_common_prefix(strs)
print(result)


# Time Complexity: O(n * m)
# Space Complexity: O(m)

def min_changes(s):
    changes0 = 0
    changes1 = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != "0":
                changes0 += 1
            if s[i] != "1":
                changes1 += 1
        else:
            if s[i] != "1":
                changes0 += 1
            if s[i] != "0":
                changes1 += 1
    if changes0 < changes1:
        return changes0
    return changes1

s = "0100"
result = min_changes(s)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(1)
def buddy_strings(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal:
        for ch in s:
            if s.count(ch) > 1:
                return True
        return False

    mismatch = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            mismatch.append(i)
    if len(mismatch) != 2:
        return False
    i = mismatch[0]
    j = mismatch[1]
    if s[i] == goal[j] and s[j] == goal[i]:
        return True
    return False

s = "ab"
goal = "ba"
result = buddy_strings(s, goal)
print(result)




# Time Complexity: O(n^2) in the equal-string case
# Space Complexity: O(n)
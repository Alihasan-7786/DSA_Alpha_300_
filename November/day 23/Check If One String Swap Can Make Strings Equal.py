def are_almost_equal(s1, s2):
    if len(s1) != len(s2):
        return False
    mismatch1 = -1
    mismatch2 = -1
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count == 1:
                mismatch1 = i
            elif count == 2:
                mismatch2 = i
            else:
                return False
    if count == 0:
        return True
    if count == 2:
        if s1[mismatch1] == s2[mismatch2] and s1[mismatch2] == s2[mismatch1]:
            return True
    return False

s1 = "bank"
s2 = "kanb"
result = are_almost_equal(s1, s2)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(1)
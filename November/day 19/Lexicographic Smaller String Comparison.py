def is_smaller(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] < s2[i]:
            return True
        if s1[i] > s2[i]:
            return False
        i += 1
    return len(s1) < len(s2)

s1 = "apple"
s2 = "banana"

result = is_smaller(s1, s2)
print(result)





# Time Complexity: O(min(n, m))
# Space Complexity: O(1)
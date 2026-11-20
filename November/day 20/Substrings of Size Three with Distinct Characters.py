def count_good_substrings(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
            count += 1
    return count

s = "xyzzaz"

result = count_good_substrings(s)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(1)
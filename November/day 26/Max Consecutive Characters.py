def max_power(s):
    if len(s) == 0:
        return 0
    max_count = 1
    current_count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            max_count = current_count
    return max_count

s = "abbcccddddeee"
result = max_power(s)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(1)

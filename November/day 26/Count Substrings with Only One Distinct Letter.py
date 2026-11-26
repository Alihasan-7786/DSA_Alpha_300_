def count_letters(s):
    count = 0
    current = 0
    for i in range(len(s)):
        if i == 0 or s[i] == s[i - 1]:
            current += 1
        else:
            current = 1
        count += current
    return count
  
s = "aaaba"
result = count_letters(s)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(1)

def length_of_last_word(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    count = 0
    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1

    return count

s = "Hello World"

result = length_of_last_word(s)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(1)

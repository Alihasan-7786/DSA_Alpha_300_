def count_segments(s):
    count = 0
    in_word = False
    for ch in s:
        if ch != ' ':
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count
s = "Hello, my name is John"

result = count_segments(s)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(1)
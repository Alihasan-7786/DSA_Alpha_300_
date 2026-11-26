def longest_nice_substring(s):
    best = ""
    for i in range(len(s)):
        lower_set = set()
        upper_set = set()
        for j in range(i, len(s)):
            ch = s[j]
            if ch == ch.lower():
                lower_set.add(ch)
            else:
                upper_set.add(ch.lower())
            if lower_set == upper_set:
                if j - i + 1 > len(best):
                    best = s[i:j + 1]
    return best

s = "YazaAay"
result = longest_nice_substring(s)
print(result)




# Time Complexity: O(n³) worst case
# Space Complexity: O(n)

def longest_nice_substring(s):
    best = ""
    for i in range(len(s)):
        chars = set()
        for j in range(i, len(s)):
            chars.add(s[j])
            nice = True
            for ch in chars:
                if ch.islower():
                    if chr(ord(ch) - 32) not in chars:
                        nice = False
                        break
                elif ch.isupper():
                    if chr(ord(ch) + 32) not in chars:
                        nice = False
                        break
            if nice and j - i + 1 > len(best):
                best = s[i:j + 1]
    return best

s = "YazaAay"
result = longest_nice_substring(s)
print(result)



# Time Complexity: O(n^3)
# Space Complexity: O(n)
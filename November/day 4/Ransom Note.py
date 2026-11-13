def can_construct(ransomNote, magazine):
    freq = {}
    for ch in magazine:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in ransomNote:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
      
    return True

ransomNote = "aa"
magazine = "aab"

result = can_construct(ransomNote, magazine)
print(result)


# Time Complexity: O(n + m)
# Space Complexity: O(k)

def vowel_ranges(s, queries):
    prefix = [0]
    vowels = "aeiou"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
        prefix.append(count)
    result = []
    for query in queries:
        left = query[0]
        right = query[1]
        vowel_count = prefix[right + 1] - prefix[left]
        result.append(vowel_count)
    return result

s = "abecid"
queries = [[0, 2], [1, 4], [0, 5]]
result = vowel_ranges(s, queries)
print(result)





# Time Complexity: O(n + q)
# Space Complexity: O(n + q)
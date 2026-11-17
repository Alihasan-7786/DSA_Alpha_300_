def sum_prefix_scores(words):
    prefix_count = {}
    for word in words:
        current_prefix = ""
        for ch in word:
            current_prefix += ch
            if current_prefix not in prefix_count:
                prefix_count[current_prefix] = 0
            prefix_count[current_prefix] += 1
    result = []

    for word in words:
        current_prefix = ""
        score = 0
        for ch in word:
            current_prefix += ch
            score += prefix_count[current_prefix]
        result.append(score)

    return result

words = ["abc", "ab", "bc", "b"]
result = sum_prefix_scores(words)
print(result)




# Time Complexity: O(N * L^2)
# Space Complexity: O(N * L^2)
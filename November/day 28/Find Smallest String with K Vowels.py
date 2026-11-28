def smallest_string(k):
    vowels = "aeiou"
    result = []
    for i in range(k):
        result.append(vowels[i % 5])
    return "".join(result)

k = 5
print(smallest_string(k))




# Time Complexity: O(k)
# Space Complexity: O(k)
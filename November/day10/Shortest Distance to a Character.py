def shortest_to_char(s, c):
    n = len(s)
    result = [0] * n
    previous = -n
    for i in range(n):
        if s[i] == c:
            previous = i
        result[i] = i - previous
    previous = 2 * n
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            previous = i
        distance = previous - i
        if distance < result[i]:
            result[i] = distance
    return result

s = "loveleetcode"
c = "e"

result = shortest_to_char(s, c)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(n)
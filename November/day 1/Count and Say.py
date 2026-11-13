def count_and_say(n):
    result = "1"
    for i in range(n - 1):
        chars = []
        j = 0
        while j < len(result):
            count = 1
            while j + 1 < len(result) and result[j] == result[j + 1]:
                count += 1
                j += 1
            chars.append(str(count))
            chars.append(result[j])
            j += 1
        result = "".join(chars)
    return result

n = 4

result = count_and_say(n)
print(result)


# Time Complexity: O(n * L)
# Space Complexity: O(L)

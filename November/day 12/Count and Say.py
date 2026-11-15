def count_and_say(n):
    result = "1"
    for i in range(n - 1):
        new_result = []
        count = 1
        for j in range(1, len(result)):
            if result[j] == result[j - 1]:
                count += 1
            else:
                new_result.append(str(count))
                new_result.append(result[j - 1])
                count = 1
        new_result.append(str(count))
        new_result.append(result[-1])
        result = "".join(new_result)
    return result

n = 5
result = count_and_say(n)
print(result)





# Time Complexity: Depends on the length of generated terms
# Space Complexity: O(L), where L is the length of the generated term
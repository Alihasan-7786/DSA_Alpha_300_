def add_strings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += ord(num1[i]) - ord('0')
            i -= 1
        if j >= 0:
            total += ord(num2[j]) - ord('0')
            j -= 1
        result.append(chr(total % 10 + ord('0')))
        carry = total // 10
    answer = []
    for k in range(len(result) - 1, -1, -1):
        answer.append(result[k])
    return "".join(answer)

num1 = "11"
num2 = "123"
result = add_strings(num1, num2)
print(result)



# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m))

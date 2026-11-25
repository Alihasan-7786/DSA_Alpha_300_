def add_binary(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total m+= int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))
        carry = total // 2
    answer = []
    for k in range(len(result) - 1, -1, -1):
        answer.append(result[k])
    return "".join(answer)

a = "1010"
b = "1011"
result = add_binary(a, b)
print(result)




# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m))

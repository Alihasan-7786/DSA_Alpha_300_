def to_hex(num):
    if num == 0:
        return "0"
    if num < 0:
        num += 2 ** 32
    digits = "0123456789abcdef"
    result = []
    while num > 0:
        remainder = num % 16
        result.append(digits[remainder])
        num //= 16
    answer = []
    for i in range(len(result) - 1, -1, -1):
        answer.append(result[i])
    return "".join(answer)

num = 26
result = to_hex(num)
print(result)




# Time Complexity: O(1) for 32-bit integers
# Space Complexity: O(1) for 32-bit integers

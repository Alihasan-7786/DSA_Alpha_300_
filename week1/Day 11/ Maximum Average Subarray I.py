def find_max_average(numbers, k):
    total = 0
    for i in range(k):
        total += numbers[i]
    max_sum = total
    for i in range(k, len(numbers)):
        total = total + numbers[i] - numbers[i - k]
        if total > max_sum:
            max_sum = total
    return max_sum / k

numbers = [1, 12, -5, -6, 50, 3]
k = 4

result = find_max_average(numbers, k)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(1)
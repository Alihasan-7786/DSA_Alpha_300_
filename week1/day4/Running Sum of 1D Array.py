def running_sum(numbers):
    result = []
    total = 0

    for num in numbers:
        total += num
        result.append(total)

    return result


numbers = [1, 2, 3, 4]

result = running_sum(numbers)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(n)

def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    for num in frequency:
        print(num, "appears", frequency[num], "times")

numbers = [1, 2, 2, 3, 1, 4, 2]

count_frequency(numbers)


# Time Complexity: O(n)
# Space Complexity: O(n)
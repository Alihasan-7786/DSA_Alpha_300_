def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
def rotate_array(numbers, k):
    n = len(numbers)
    if n == 0:
        return numbers
    k = k % n
    cycles = gcd(n, k)
    for start in range(cycles):
        current = start
        previous = numbers[start]
        while True:
            next_index = (current + k) % n
            temp = numbers[next_index]
            numbers[next_index] = previous
            previous = temp
            current = next_index
            if current == start:
                break
    return numbers

numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3

result = rotate_array(numbers, k)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(1)
def ship_within_days(weights, days):
    low = 0
    high = 0
    for weight in weights:
        if weight > low:
            low = weight
        high += weight
    while low < high:
        capacity = low + (high - low) // 2
        current_load = 0
        required_days = 1
        for weight in weights:
            if current_load + weight > capacity:
                required_days += 1
                current_load = 0
            current_load += weight
        if required_days <= days:
            high = capacity
        else:
            low = capacity + 1
    return low

print(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(ship_within_days([3, 2, 2, 4, 1, 4], 3))
print(ship_within_days([1, 2, 3, 1, 1], 4))



# Time Complexity: O(n * log(sum(weights)))
# Space Complexity: O(1)
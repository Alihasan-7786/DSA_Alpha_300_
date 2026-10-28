def min_eating_speed(piles, h):
    low = 1
    high = 0
    for pile in piles:
        if pile > high:
            high = pile
    while low < high:
        speed = low + (high - low) // 2
        hours = 0
        for pile in piles:
            hours += pile // speed
            if pile % speed != 0:
                hours += 1
        if hours <= h:
            high = speed
        else:
            low = speed + 1
    return low

print(min_eating_speed([3, 6, 7, 11], 8))
print(min_eating_speed([30, 11, 23, 4, 20], 5))
print(min_eating_speed([30, 11, 23, 4, 20], 6))



# Time Complexity: O(n * log(max(piles)))
# Space Complexity: O(1)
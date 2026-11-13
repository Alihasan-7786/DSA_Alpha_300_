def num_jewels_in_stones(jewels, stones):
    jewel_set = set()
    for ch in jewels:
        jewel_set.add(ch)
    count = 0
    for ch in stones:
        if ch in jewel_set:
            count += 1

    return count

jewels = "aA"
stones = "aAAbbbb"

result = num_jewels_in_stones(jewels, stones)
print(result)


# Time Complexity: O(n + m)
# Space Complexity: O(k)

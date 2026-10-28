def allocate_minimum_pages(pages, students):
    if students > len(pages):
        return -1
    low = 0
    high = 0
    for page_count in pages:
        if page_count > low:
            low = page_count
        high += page_count
    while low < high:
        limit = low + (high - low) // 2
        used_students = 1
        current_pages = 0
        for page_count in pages:
            if current_pages + page_count > limit:
                used_students += 1
                current_pages = 0
            current_pages += page_count
        if used_students <= students:
            high = limit
        else:
            low = limit + 1
    return low

print(allocate_minimum_pages([12, 34, 67, 90], 2))
print(allocate_minimum_pages([15, 17, 20], 2))
print(allocate_minimum_pages([10, 20], 3))




# Time Complexity: O(n * log(sum(pages)))
# Space Complexity: O(1)
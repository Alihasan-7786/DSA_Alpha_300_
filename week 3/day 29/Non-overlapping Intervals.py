def erase_overlap_intervals(intervals):
    n = len(intervals)
    for i in range(1, n):
        current = intervals[i]
        j = i - 1
        while j >= 0 and intervals[j][1] > current[1]:
            intervals[j + 1] = intervals[j]
            j -= 1
        intervals[j + 1] = current
    removed = 0
    end = intervals[0][1] if n > 0 else 0
    for i in range(1, n):
        if intervals[i][0] < end:
            removed += 1
        else:
            end = intervals[i][1]
    return removed

print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))
print(erase_overlap_intervals([[1, 2], [2, 3]]))



# Time Complexity: O(n^2)
# Space Complexity: O(1) auxiliary space

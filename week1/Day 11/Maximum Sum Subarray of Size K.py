def max_sum_subarray(nums, k):
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum = current_sum + nums[i] - nums[i - k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 3

result = max_sum_subarray(nums, k)
print(result)

# Time Complexity: O(n)
# Space Complexity: O(1)

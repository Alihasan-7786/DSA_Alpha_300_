class NumArray:
    def __init__(self, numbers):
        self.prefix = [0]
        total = 0
        for num in numbers:
            total += num
            self.prefix.append(total)
    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

numbers = [-2, 0, 3, -5, 2, -1]

obj = NumArray(numbers)

print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))




# Time Complexity: O(n + q)
# Space Complexity: O(n)
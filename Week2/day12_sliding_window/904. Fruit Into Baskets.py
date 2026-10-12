class Solution:
    def totalFruit(self, fruits):
        left = 0
        first = -1
        second = -1
        count1 = 0
        count2 = 0
        result = 0
        for right in range(len(fruits)):
            fruit = fruits[right]
            if fruit == first:
                count1 += 1
            elif fruit == second:
                count2 += 1
            elif count1 == 0:
                first = fruit
                count1 = 1
            elif count2 == 0:
                second = fruit
                count2 = 1
            else:
                while count1 > 0 and count2 > 0:
                    old = fruits[left]
                    if old == first:
                        count1 -= 1
                    else:
                        count2 -= 1
                    left += 1
                if count1 == 0:
                    first = fruit
                    count1 = 1
                else:
                    second = fruit
                    count2 = 1
            length = right - left + 1
            if length > result:
                result = length
        return result
fruits = [1, 2, 1, 2, 3]
obj = Solution()
print(obj.totalFruit(fruits))

def count_matches(items, ruleKey, ruleValue):
    count = 0
    if ruleKey == "type":
        index = 0
    elif ruleKey == "color":
        index = 1
    else:
        index = 2
    for item in items:
        if item[index] == ruleValue:
            count += 1
    return count

items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"]
]
ruleKey = "color"
ruleValue = "silver"

result = count_matches(items, ruleKey, ruleValue)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(1)
nums = [15, 85, 65, 45, 15, 78, 65, 15]
# nums = [1, 2, 3, 2, 1, 3, 5, 1]
new_nums = []

for x in range(len(nums)):
    for y in range(x, len(nums)):
        if nums[x] == nums[y] and x != y:
            nums[y] = None

for x in range(len(nums)):
    if nums[x] != None:
        new_nums.append(nums[x])

del nums
print(new_nums)

nums = [12, 45, 7, 89, 23]

largest = nums[0]

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]

print(largest)
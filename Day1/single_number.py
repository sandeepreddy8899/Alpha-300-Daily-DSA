nums = [4, 1, 2, 1, 2]

for i in range(len(nums)):
    count = 0

    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1

    if count == 1:
        print(nums[i])
        break
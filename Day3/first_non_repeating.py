nums = [4, 5, 1, 2, 1, 4, 5]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num in nums:
    if freq[num] == 1:
        print(num)
        break
else:
    print(-1)
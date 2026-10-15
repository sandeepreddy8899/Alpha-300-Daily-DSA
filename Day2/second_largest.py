nums = [12, 45, 7, 89, 23]

largest = float('-inf')
second = float('-inf')

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("No second largest element")
else:
    print(second)
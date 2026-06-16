nums = [10, 25, 5, 40, 30]

largest = second = float("-inf")

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest:", second)
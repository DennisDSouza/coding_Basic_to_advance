nums = [10, 25, 5, 40, 30]

largest = nums[1]

for num in nums:
    if num > largest:
        largest = num

print("Largest:", largest)
nums = [0, 1, 0, 3, 12]

result = []

for i in nums:
    if i != 0:
        result.append(i)

while len(result) < len(nums):
    result.append(0)

print(result)
nums = [1, 2, 4, 5,7,12]

n = 12

for i in range(1, n + 1):
    if i not in nums:
        print("Missing Number:", i)
nums = [2,1,5,1,3,2]
k = 3

window_sum = sum(nums[:k])
maximum = window_sum

for i in range(k, len(nums)):
    window_sum = window_sum + nums[i] - nums[i-k]
    maximum = max(maximum, window_sum)

print(maximum)
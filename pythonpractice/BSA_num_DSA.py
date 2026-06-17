nums = [1, 2, 3, 4, 5, 6, 7]
target = 5

start = 0
end = len(nums) - 1

while start <= end:
    mid = (start + end) // 2

    if nums[mid] == target:
        print("Found")
        break

    if target > nums[mid]:
        start = mid + 1
    else:
        end = mid - 1
        
        
        
        
nums = [1, 2, 3, 4, 5, 6, 7]
target = 5

if target in nums:
    print("Found at index", nums.index(target))
else:
    print("Not Found")
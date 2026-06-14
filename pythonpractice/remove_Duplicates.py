num=[1,2,3,3,4,5,6]

result=[]

for nums in num:
    
    if nums not in result:
        result.append(nums)
        
print(" the correct nums",result)
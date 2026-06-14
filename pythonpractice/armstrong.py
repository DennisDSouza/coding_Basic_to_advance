num = 153 
# 0,1,153,370,371,407

temp = num
total = 0

while num > 0:
    digit = num % 10
    total = total + digit**3
    num = num // 10

if temp == total:
    print("Armstrong")
else:
    print("Not Armstrong")
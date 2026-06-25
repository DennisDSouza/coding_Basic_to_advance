num =16

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Non Prime")
    
    
    
num=123
count=0
for gets in range(1,num+1):
    if num%gets==0:
        count+1
if count==2:
            print("its is prime ")
else:
            print("its not prime")
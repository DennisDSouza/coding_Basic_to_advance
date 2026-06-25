num=[1,2,3,3,4,5,6]

result=[]

for nums in num:
    
    if nums not in result:
        result.append(nums)
        
print(" the correct nums",result)



nume=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for nums in nume:
    if nums %2==0:
         even=even+1
    else:
          odd=odd+1
print(even)
print(odd)

num =12345 
store=0
while num>0:
    digit=num%10
    store=store*10+digit
    num=num//10
print(store)

c="dennis dsoiza"
store=""
for ch in c:
    store=ch+store
print(store)

panlin=121
tem=panlin
num=0
while panlin > 0:
    digit=panlin % 10
    num=num*10+digit
    panlin=panlin // 10
    
if tem==num:
    print("panlindrom")
else:
    print("not panlindrom ")
    
ch ="malayalam"
tem=""
for i in ch:
    tem =i+tem
if tem==ch:
       print("the charater is panlindron")
else:
        print("the charater is not panlindrom")
        
        
i=7
factorial=1
while i>0:
    factorial=factorial*i
    i=i-1
print(factorial)
        
num=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for gets in num:
    if gets %2==0:
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)

cha="denis"
tem=0
for i in cha:
    if i in "aieou":
     tem =tem+1
print(tem)
        

num=[1,2,3,4,5,6,6,4,5,6]
tem=[]
for ch in num:
    if ch not in tem:
        tem.append(ch) 
print(tem)
    
num =2345465
stre=0
while num>0:
    digit=num%10
    stre=stre*10+digit
    num=num//10
print(stre)

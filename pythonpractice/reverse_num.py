num=12344

stored=0

while num >0:
    
    digit=num%10
    stored=stored*10+digit
    num=num//10
    
print(stored)

num=54321
store=0
while num>0:
    digit=num%10
    store=store*10+digit
    num=num//10
print(store)

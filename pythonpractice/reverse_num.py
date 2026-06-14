num=12344

stored=0

while num >0:
    
    digit=num%10
    stored=stored*10+digit
    num=num//10
    
print(stored)
num=121

demo_store=num
rev=0

while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
    
if demo_store==rev:
    
    print("the number is palindrom")
    
else:
    
    print("the number is not panlindrom")
    

    
    
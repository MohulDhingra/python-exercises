'''a=input("Enter a character: ")
b=ord(a)
print(b)
c=-1
if b>=65 and b<=90 or b>=97 and b<=122:
    print("Albhabet")
    c=1
if b>=48 and b<=57:
    print("Number")
    c=1
if c==-1:
    print("Special characater")'''
'''a=int(input("Enter electricity units: "))
if a>=0 and a<=50:
    b=a*0.50
    print(b)
if  a>50 and a<=150:
    b=a*0.75
    print(b)
if a>150 and a<=250:
    b=a*1.20
    print(b)
if a>250:
    b=a*1.50
    print(b)'''
'''a=int(input("Enter the amount: "))
b=c=d=e=0
if a>=500:
    b=int(a/500)
    a=a-(b*500)
if a>=200:
    c=int(a/200)
    a=a-(c*200)
if a>=100:
    d=int(a/100)
    a=a-(d*100)
if a>=10:
    e=int(a/10)
    a=a-(e*10)
print("500 notes",b)
print("200 notes",c)
print("100 notes",d)
print("10 notes",e)'''
a=input("Enter your password: ")
c=a.split()
print(c)
b=len(a)
if b>=4:
    print(c)
    
        
    
    
else:
    print("Invalid length")
            
    
    
    
    
    


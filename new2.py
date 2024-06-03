'''a=input("Enter a number: ")
b=str(a)
if '.' in b:
    print("Number is float")
else:
    print("Number is integer")'''
'''a=int(input("Enter a number: "))
if a%5==0 and not a%7==0:
        print("Yes")
if a%7==0 and not a%5==0:
        print("No")
if a%5==0 and a%7==0:
        print("Yo")
if a%5!=0 and a%7!=0:
    print("Why")'''
'''a=float(input("Enter your marks: "))
if a<33 :
    print("Your grade is F")
if a<=50 and a>=33 :
    print("Your grade is C")
if a<=70 and a>33 and a>50:
    print("Your grade is B")
if a<=100 and a>70 and a>50 and a>33 :
    print("Your grade is A")'''
a=float(input("Enter the 1st side of Triangle: "))
b=float(input("Enter the 2nd side of Triangle: "))
c=float(input("Enter the 3rd side of Triangle: "))
if a==b==c:
    print("It is an equilateral Triangle")
if a==b!=c or a!=b==c or a==c!=b:
     print("It is an isosceles Triangle")
elif a!=b!=c:
     print("It is an scalar Triangle")

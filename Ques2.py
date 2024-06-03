'''#Given year is leap year or not
a=int(input("Enter the year: "))
if a%4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
'''
'''#To find the quadrant of the given point
a=int(input("Enter the coordinate of abscissa: "))
b=int(input("Enter the coordinate of ordinate: "))
if a>0 and b>0:
    print("1st quadrant")
elif a<0 and b>0:
    print("2nd quadrant")
elif a>0 and b<0:
    print("4th quadrant")
elif a<0 and b<0:
    print("3rd quadrant")
'''    
#Reverse alphabets i.e from Z to A




'''#Positive number and its multiplcation upto 10
a=int(input("Enter a positive number: "))
if a<0:
    print("Error")
elif a>0:
    i=1
    while i<11:
        b=a*i
        print(b)
        i=i+1
'''    
'''#whether it is alpha,no,special character
a=input("Enter a character: ")
b=ord(a)
c=0
if b>=65 and b<=90 or b>=97 and b<=122:
    print("Albhabet")
    c=1
if b>=48 and b<=57:
    print("Number")
    c=1
if c==0:
    print("Special characater")
'''
'''# Count number of digits
a=int(input("Enter a number: "))
c=str(a)
b=len(c)
print("Number of digits =",b)'''
'''#Finding factorial
a=int(input("Enter a number: "))
if a<0:
    print("No factorial possible")
elif a==1 or a==0:
    print("Factorial is 1")
elif a>0:
    i=a
    while i>0:
        i=a*(a-1)
        print(i)
'''
'''# Sum and Average of 10 numbers
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
d=int(input("Enter the 4th number: "))
e=int(input("Enter the 5th number: "))
f=int(input("Enter the 6th number: "))
g=int(input("Enter the 7th number: "))
h=int(input("Enter the 8th number: "))
i=int(input("Enter the 9th number: "))
j=int(input("Enter the 10th number: "))
sum=a+b+c+d+e+f+g+h+i+j
print("Sum is =",sum)
average=(a+b+c+d+e+f+g+h+i+j)/10
print("Average is =",average)
'''
'''#Number is PALINDROME or not
a=input("Enter a number: ")
b=a[::-1]
if a==b:
    print("Number is Palindrome")
if a!=b:
    print("Number is not Palindrome")
'''

#Decimal to Binary number

number=int( input("Enter decimal number: "))
items=[]


while number>0:

    items.append(int(number)%2)

    number=int(number)//2

    
items.reverse()

print(items)

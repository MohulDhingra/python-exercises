'''x=5
def A():
    x=3
    print(x)



print(A())
print(x)'''
'''def A():
    x=5
    def B():
        nonlocal x
        print("hi")
        print(x)
    print("Yes")
    B()
    print("Sky")
print("Wow")
x=A()
print(x)
'''
'''def count(i):
    print(i)
    i=i-1
    if i>0:
        count(i)


count(10)
'''
'''x=int(input("Enter a number: "))
def count(i,x):
    print(i*x)
    i=i+1
    if i<=10:
        count(i,x)

count(1,x)
'''
'''def x():
    print("Yes")
    print("Hi")
    yield 5
    print("Yo")
    print("Why")
    yield 20
p=x()
print(next(p))
print(next(p))
'''
'''x=[1,2,3]
p=x.__iter__()
print(next(p))
print(next(p))
'''
'''def x(*kwargs):
    print(kwargs)

x(1,2,3)
x(1,2)
'''
'''a=int(input("Enter a number: "))
x=lambda a:a%5==0
print(x(a))
'''

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
def x(a):
    while a<b:
        a=a+1
        print(a)
    while a>b:
        a=a-1
        print(a)
x(a)

a=int(input("Enter 1st number: "))

        



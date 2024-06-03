'''class Infra:
    room= 106
    name= None
    age= None
    qty= None
    def __init__(self):
      print("1st")
    def __init__(self,x):
        print("2nd")

x=Infra(2)'''
'''class Infra:
    def hi():
        print("HI")
p=staticmethod(Infra.hi)
p()
'''
class student():
    def __init__(self):
        self.name=input("Enter Name: ")
        self.roll=int(input("Enter roll no.: "))
        self.marks=int(input("Enter Marks: "))
    def print(self):
        print(self.name)
        print(self.roll)
        print(self.marks)

students=[]
for i in range(0,2):
    students.append(student())
for i in range(0,2):
    students[i].print()

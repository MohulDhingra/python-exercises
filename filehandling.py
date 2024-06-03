import os
a=input("Enter drive name: ")
b=input("Enter folder name: ")
try:
    f=open(a+":/"+b+".txt","r")
    item=f.readlines()
    for i in item:
        print(i)
    x=os.path.getsize(a+":/"+b+".txt")
    print("File Size is :",x)

    


except:
    print("File not found")

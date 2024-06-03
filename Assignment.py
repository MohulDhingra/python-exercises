'''try:
    a=int(input("Enter a no: "))
    x=[0,0,1]
    print("no. is",x[a]/0)
except ValueError:
    print("Invalid no")
except IndexError:
    print("Invalid index")
except:
    print("invalid unknown")
'''
'''while True:
    try:
        a=int(input("Enter no: "))
        print(a)
        break
    except:
        print("Invalid")'''
from datetime import datetime
print(datetime.now())

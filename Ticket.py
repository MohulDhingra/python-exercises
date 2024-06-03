a=input("Enter your Ticket code: ")
b=str(a)
c=len(b)
if c==5:
    if a.startswith ('AB') or  a.startswith ('TM'):
        d=a[2: ]
        if a.startswith ('AB'):
            e=int(d)+10
            print("Price is",e)
        if a.startswith ('TM'):
            f=int(d)-10
            print("Price is",f)
            
        
    else:
        print("Error:\" invalid starting\"")
    
else:
    print("Error:\" invalid length\"")

a=int(input("Enter no of steps: "))
b=input("Enter the starting step: ")
if b=="top":
    if a%2==0:
        print("Winner is Tip")
    if a%2!=0:
        print("Winner is Top")
if b=="tip":
    if a%2==0:
        print("Winner is Top")
    if a%2!=0:
        print("Winner is Tip")

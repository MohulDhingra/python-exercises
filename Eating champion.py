import random
class champion:
    current=0
    fixed=300
    spoon=random.randrange(1,100)
    def eat(self):
        qty=int(input("How much to eat?: "))
        if qty>self.spoon:
            return -1
        else:
            self.current=self.current+qty
            if self.current>=self.fixed:
                    print("You win")
                    return 2
                
step=0
champ=champion()
while True:
    x=champ.eat()
    if x==-1:
        print('''Too much to eat
              YOU LOSE''')
        break
    if x==2:
        print("You won in",step)
        break
    step=step+1
    
        
            
'''print(random.randrange(1,100))'''

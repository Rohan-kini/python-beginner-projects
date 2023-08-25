import random

def gamewin(comp,you):
    if comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=='s':
            return True
        elif you=='r':
            return False
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False
    else:
        return None
    

print("***WELCOME TO ROCK/PAPER/SCISSOR GAME***")
print()
matches=int(input("Enter matches you want to play in the series(odd number plz):"))
i=1
yourscore=0
computerscore=0

while(i<=matches):
    print(f"Computer's turn:rock(r) paper(p) scissor(s)")
    randcomp=random.randint(1,3)
    if randcomp==1:
         comp='r'
    elif randcomp==2:
        comp='p'
    else:
        comp='s'
    print(f"Your turn:rock(r) paper(p) scissor(s)")
    you=input()
    print(f"Computer chose:{comp}")
    print(f"You chose:{you}")
    result=gamewin(comp,you)
    if result==None:
         yourscore=yourscore+0
         computerscore=computerscore+0
    elif result==True:
        yourscore=yourscore+1
    else :
        computerscore=computerscore+1
    i=i+1
print()
print("***RESULT TIME***")
print("YOUR SCORE:",yourscore)
print("COMPUTER SCORE:",computerscore)
if yourscore>computerscore:
    print("YOU WIN!")
elif computerscore>yourscore:
    print("COMPUTER WIN! BETTER LUCK NEXT TIME")
else:
    print("NAIL BITING SERIES COMES TO AN END WITH A DRAW")

        











'''
When we were kids, we had games to play. But we lost the small dice needed for one game,
so we couldn't play it. Now there's good news we've created an online dice simulator!
Now,no need to worry anymore. We can enjoy the game again!
'''

import random

roll=True
def diceart(dice):
    if dice==1:
        print(" _______")
        print("|       |")
        print("|   o   |")
        print("|_______|")
    elif dice==2:
        print(" _______")
        print("|       |")
        print("|  o o  |")
        print("|_______|")
    elif dice==3:
        print(" _______")
        print("|   o   |")
        print("|   o   |")
        print("|   o   |")
        print("|_______|")
    elif dice==4:
        print(" _______")
        print("|  o o  |")
        print("|  o o  |")
        print("|_______|")
    elif dice==5:
        print(" _______")
        print("|  o o  |")
        print("|   o   |")
        print("|  o o  |")
        print("|_______|")
    elif dice==6:
        print(" _______")
        print("| o o o |")
        print("| o o o |")
        print("| o o o |")
        print("|_______|")







while roll:
    dice=(random.randint(1,6))
    diceart(dice)
    rollmoretime=input("Want to roll one more time (y/n):")
    if rollmoretime=='y':
        roll=True
    else:
        roll=False

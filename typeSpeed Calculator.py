from time import*
import random as r

def mistake(test1,test2):
    error=0
    try:
        for i in range(len(test1)):
            if test1[i]!=test2[i]:
               error=error+1
    except:
        error=error+1
    return error 

def timetaken(time_1,time_2,test2):
    time_delay=time_2-time_1
    time_final=round(time_delay,2)
    speed=len(test2)/time_final
    return round(speed,2)

test=['my name is rohan','studying engineering','i love cricket and badminton','rp17 is love','save water']
test1=r.choice(test)
print(test1)
time_1=time()
test2=input("Enter:")
time_2=time()

print("Speed calculated is:",timetaken(time_1,time_2,test2),"w/sec")
print("Errors:",mistake(test1,test2))
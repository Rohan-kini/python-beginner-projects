import time

countdown=int(input("Enter time in seconds:"))

for x in range(countdown,0,-1):
    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)##gives a delay of 1 second and thats what we need in countdown..

print("TIME's UP!")
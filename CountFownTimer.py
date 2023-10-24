import time


def countdown(t):
    while t:
        mins, secs = divmod((t), 60)

        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Ready to go")



choice=int(input('''Enter Time :-
                     For In Hour 1:
                     For In Minute 2 :
                     For In Second 3    :-'''))
print()
if choice==1:
    Hour = int(input("Enter time in Hour"))
    t=Hour*3600
    countdown(int(t))
    
elif choice==2:
    Minute = int(input("Enter time in Minute"))
    t=Minute*60
    countdown(int(t))
    
else:
    Second= int(input("Enter time in second"))
    t=Second
    countdown(int(t))
    




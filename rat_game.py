import random
import threading
import time
import keyboard as key

#prints rat at a random time and starts a one second timer for the user to react
def rat():
    rat.a=0
    rat.c=0
    for i in range(1,100):
        rat.a=random.randint(1,100)
        if int(rat.a)%2==0:
            rat.b=time.sleep(random.randint(1,5))
            print("rat")
            rat.c="rat"
            timer=threading.Timer(1.0,keyboard)
            timer.start()
            break
        
#Universal variable
score=0

#checks if the user is pressing the esc key while rat is printed and updates the score 
def keyboard():
    global score
    keyboard.d=key.is_pressed('esc')
    if rat.c=="rat" and keyboard.d==True:
        print("you caught the rat!")
        score=score+1
        print(f"your score is: ",score)
        rat()
    else:
        print(f"you missed the rat!")
        print(f"your score is: ",score)
                    
#_main_        
rat() 

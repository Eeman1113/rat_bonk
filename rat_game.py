import random
import threading
import time
import keyboard as key


def rat():
    rat.a=0
    rat.c=0
    rat.score=0
    for i in range(1,100):
        rat.a=random.randint(1,100)
        if int(rat.a)%2==0:
            rat.b=time.sleep(random.randint(1,5))
            print("rat")
            rat.c="rat"
            timer=threading.Timer(2.0,keyboard)
            timer.start()
            break
def keyboard():
    keyboard.d=key.is_pressed('esc')
    if rat.c=="rat" and keyboard.d==True:
        print("you caught the rat")
        rat.score=rat.score+1
        print(f"your score is: ",rat.score)
        rat()
    else:
        print(f"you missed the rat")
        print(f"your score is: ",rat.score)
                    
#_main_        
rat() 

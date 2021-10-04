#Automatic Mouse Clicker, Josiah Schmidt, Last Edited 1/11/2019
#Future changes- add a way to while loop and press a key to break loop
#WINDOWS ONLY
import ctypes
import time

def click():
    for i in range (5000):                              #loop 5000 times, roughly 20s
        ctypes.windll.user32.SetCursorPos(275,400)      #move mouse to 275,400 position
        ctypes.windll.user32.mouse_event(2,0,0,0,0)     #mouse left click down
        ctypes.windll.user32.mouse_event(4,0,0,0,0)     #mouse left click up
        time.sleep (0.00001)                            #prevents the system from crashing, don't remove this


go=str(input("type start to start: "))
while(go=="start"):
    click()
    go=str(input("go again? 'start' to go: "))

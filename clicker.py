import ctypes
import time

for i in range (3000):
    ctypes.windll.user32.SetCursorPos(275,400)
    ctypes.windll.user32.mouse_event(2,0,0,0,0)
    ctypes.windll.user32.mouse_event(4,0,0,0,0)
    time.sleep (0.00001)
    
#500 cycles per second
#30,000 cycles per minute

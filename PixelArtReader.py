import win32api
import time
import os, sys

lines = open(sys.argv[1],"rt").readlines()
for a in lines:
    os.system("cls")
    print(a)
    time.sleep(0.5)
    pressed = False
    while not pressed:
        if win32api.GetAsyncKeyState(ord('K')):
            pressed = True
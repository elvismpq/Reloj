import os
import time
from time import sleep
def cls():
    os.system('cls')
print(time.localtime())
s=0
while s==0:
    t = time.localtime()
    hour = t[3]
    min = t[4]
    sec = t[5]
    print("La hora es: ",hour, ":", min, ":", sec)
    sleep(1)
    cls()

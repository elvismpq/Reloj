import os
import time
while True:
    t = time.localtime()
    hour = t[3]
    min = t[4]
    sec = t[5]
    print("La hora es: ",hour, ":", min, ":", sec)
    time.sleep(1)
    os.system('cls')

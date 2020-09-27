import time

import threading

def clock():
    while True:
        print(time.ctime())
        time.sleep(2)

def echo():
    while True:
        message = input()
        print(message.upper())

threading.Thread(target=clock).start()
threading.Thread(target=echo).start()




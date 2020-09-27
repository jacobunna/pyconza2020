import time
import select
from sys import stdin

def clock_echo():
    start = time.time()
    i = 0
    while True:
        # Clock
        if (time.time() - start) // 2 == i:
            print(time.ctime())
            i += 1

        # Echo
        available, _, _ = select.select([stdin], [], [], 0)
        if available:
            print(input().upper())

clock_echo()

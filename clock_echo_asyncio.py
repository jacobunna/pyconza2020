import asyncio
from sys import stdin
import time

async def clock():
    while True:
        print(time.ctime())
        await asyncio.sleep(2)

def echo():
    print(input().upper())

async def main():
    asyncio.get_event_loop().add_reader(stdin, echo)
    await clock()

asyncio.run(main())

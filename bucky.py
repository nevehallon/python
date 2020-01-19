import asyncio
import time

async def display_time():
    start_time = time.time()

    while True:
        dur = int(time.time() - start_time)

        if dur % 3 == 0:
            print("{} seconds have passed".format(dur))

async def print_nums():
    num = 1

    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)
async def main():
    task1 = asyncio.create_task(display_time())
    task2 = asyncio.create_task(print_nums())

    await asyncio.gather(task1, task2)


asyncio.run(main())



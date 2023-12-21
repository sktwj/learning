# -*- coding: utf-8 -*-

import asyncio, time

async def main():
    task1 = asyncio.create_task(asyncio.sleep(3))
    task2 = asyncio.create_task(asyncio.sleep(3))
    task3 = asyncio.create_task(asyncio.sleep(3))

    await task1
    await task2
    await task3

start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print("总耗时:", end - start)

# def t1():
#     start = time.time()
#     while time.time() - start < 60:
#         print("alive")
#         time.sleep(1)
#     elapsed = time.time() - start
#     print(f"timeout!!! {elapsed}s")
#
# def t2():
#     start = time.perf_counter()
#     while time.perf_counter() - start < 60:
#         print("alive")
#         time.sleep(1)
#     elapsed = time.perf_counter() - start
#     print(f"timeout!!! {elapsed}s")


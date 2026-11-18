import asyncio
import threading
import time
import multiprocessing

# Asyncio
async def async_task():
    print("Asyncio Task Started")
    await asyncio.sleep(2)
    print("Asyncio Task Completed")

async def main():
    await asyncio.gather(async_task(), async_task())


# Threading
def thread_task():
    print("Threading Task Started")
    time.sleep(2)
    print("Threading Task Completed")


# Multiprocessing
def process_task():
    print("Multiprocessing Task Running")


if __name__ == "__main__":

    # Run Asyncio
    asyncio.run(main())

    # Run Threading
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # Run Multiprocessing
    p1 = multiprocessing.Process(target=process_task)
    p2 = multiprocessing.Process(target=process_task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
import asyncio

counter = 0

async def increment():
    global counter
    for _ in range(10000):
        # BUG 1: nincs concurrency-safe művelet
        counter += 1

async def decrement():
    global counter
    for _ in range(5000):
        # BUG 2: ugyanaz a globális változó, lock nélkül
        counter -= 1

async def faulty_task():
    # BUG 3: elfelejtett await → a függvény nem fut le
    increment()

async def run_async_complex():
    global counter
    counter = 0
    await asyncio.gather(
        increment(),
        decrement(),
        faulty_task(),
    )
    return counter


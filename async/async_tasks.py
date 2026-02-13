import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fectch data")
    await asyncio.sleep(sleep_time) 
    print("Data fetched, id:", id)
    return {
        "id": id,
        "data": f"Sample data from coroutine {id}"
    }


async def main():
    # create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1, 7))
    task2 = asyncio.create_task(fetch_data(2, 10))
    task3 = asyncio.create_task(fetch_data(3, 5))

    result1 = await task1
    result2 = await task2
    result3 = await task3  
    

# Run the main coroutine
asyncio.run(main())
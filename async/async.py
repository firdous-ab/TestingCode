import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print("Fetching data....id:", id)
    await asyncio.sleep(delay) 
    # Simulate an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {
            "data": "Some data", 
            "id": id
            }
    # return some data



# coroutine function: coroutine function returns a coroutine object when called (main() --> Coroutine object)
async def main():
    print("Start of main coroutine")
    # create coroutine object
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result1 = await task1
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}")

    

# Run the main coroutine
asyncio.run(main())
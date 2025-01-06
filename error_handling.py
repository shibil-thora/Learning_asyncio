import asyncio 

async def might_fail() :
    try: 
        await asyncio.sleep(3)
        print("Success")
    except asyncio.CancelledError: 
        print("Operation cancelled")
    

async def main(): 
    task = asyncio.create_task(might_fail())

    try: 
        await asyncio.wait_for(task, timeout=2)
    except asyncio.TimeoutError: 
        print("Operation timed out")
        task.cancel() 
        await task 
    
if __name__ == "__main__": 
    asyncio.run(main())
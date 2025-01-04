import asyncio 

async def long_operation(n): 
    print(f'started operation {n}') 
    await asyncio.sleep(n) 
    print('operation complete', n) 


async def main(): 
    task1 =  asyncio.create_task(long_operation(2))
    task2 = asyncio.create_task(long_operation(4)) 

    await task1 
    await task2

if __name__ == '__main__': 
    asyncio.run(main())
import aiohttp 
import asyncio 


async def fetch(url): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url) as response: 
            return await response.text() 


async def main(): 
    url = "https://jsonplaceholder.typicode.com/todos/1"
    result = await fetch(url) 
    print(result)


if __name__ == '__main__': 
    asyncio.run(main())
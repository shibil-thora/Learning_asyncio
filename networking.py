import asyncio 

async def echo(reader, writer): 
    while True: 
        data = await reader.read(100)
        if not data: 
            break 
    
        writer.write(data)
        await writer.drain() 
    
    writer.close() 
    await writer.wait_closed() 

async def main(): 
    server = await asyncio.start_server(echo, "127.0.0.1", 8888) 

    async with server: 
        await server.serve_forever() 
    
if __name__ == '__main__': 
    asyncio.run(main())
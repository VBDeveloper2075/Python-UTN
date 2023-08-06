import asyncio

async def mostrar_s():
    while True:
        for i in range(60):
            print(i, 's')
            await asyncio.sleep(1)

async def mostrar_m():
    for i in range(1, 2):
        await asyncio.sleep(60)
        print(i, 'minuto')
    
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(mostrar_s(), mostrar_m()))
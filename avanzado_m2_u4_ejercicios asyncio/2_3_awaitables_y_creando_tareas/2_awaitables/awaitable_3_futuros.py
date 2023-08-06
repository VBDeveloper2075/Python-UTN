import asyncio

async def buscar_datos():
    print('Inicio de busqueda')
    await asyncio.sleep(1)
    return {'nombre':"Anna"}  # a Future

async def main():
    #Cuando retorna el valor crea un future
    task1 = asyncio.create_task(buscar_datos())   

    # para esperar el valor futuro uso await
    value = await task1
    print(value)

asyncio.run(main())
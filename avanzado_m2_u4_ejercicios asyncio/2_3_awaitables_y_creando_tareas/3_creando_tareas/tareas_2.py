import asyncio

async def retorna_datos():
    print('Inicio')
    await asyncio.sleep(2)
    print("hecho")
    return {'dato':1}            # a Future

async def imprime_numeros():
    for i in range(7):
        print(i)
        await asyncio.sleep(0.5)
     
async def main():

    #Cuando retorna el valor crea un future

    task1 = asyncio.create_task(retorna_datos())   
    task2 = asyncio.create_task(imprime_numeros())

    # para esperar el valor futuro uso await
    value = await task1
    await task2
    print(value)

asyncio.run(main())


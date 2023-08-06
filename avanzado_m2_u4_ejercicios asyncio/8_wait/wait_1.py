import asyncio

async def factorial(nombre, numero):
    f = 1
    for i in range(2, numero + 1):
        print(f"Tarea {nombre}: Cálculo del factorial de: ({numero}), concurrencia i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {nombre}: factorial({numero}) = {f}")
    return f

async def main():
    tasks = [
        asyncio.create_task(factorial("A", 2)),
        asyncio.create_task(factorial("B", 3)),
        asyncio.create_task(factorial("C", 4)),
    ]

    await asyncio.wait(tasks)

asyncio.run(main())
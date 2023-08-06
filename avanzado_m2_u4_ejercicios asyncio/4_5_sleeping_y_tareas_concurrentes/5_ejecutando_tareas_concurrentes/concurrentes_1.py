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
    # Almacena tres tareas concurrentes:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())
import asyncio

####################################################
# SI QUIERO ESPERAR A QUE foo() finalice puedo
# agregar await a la tarea así:
# await task
####################################################
async def main():
    print('tim')
    task=asyncio.create_task(foo('text'))
    await task
    print("finish")

async def foo(text):
    print(text)
    await asyncio.sleep(1)
     

"Con esta línea creamos un bucle de eventos y agregamos a corroutine de forma implicita"
asyncio.run(main())


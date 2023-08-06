import asyncio

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(5)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        res = await asyncio.shield(eternity())
    except asyncio.CancelledError:
        res=None

asyncio.run(main())
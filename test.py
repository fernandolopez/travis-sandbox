import asyncio

def a(a : int, b : int) -> bool:
    return a * b

assert a(2, 3) == 6

class Iterable:
    async def __anext__(self):
        if self.i == 0:
            raise StopAsyncIteration
        self.i -= 1
        await asyncio.sleep(1)
        return 42

    def __aiter__(self):
        self.i = 5
        return self

async def main():
    async for i in Iterable():
        print(i)

asyncio.run(main())

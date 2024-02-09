import asyncio


async def func1():
    print(1)
    print(2)
    asyncio.create_task(func2())
    print(3)



async def func2():
    print(4)
    for i in range(1000000000):
        continue
    print(5)


result = asyncio.run(func1())
print(result)

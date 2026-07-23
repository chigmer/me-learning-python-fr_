import asyncio
#i barely know what im doing

async def shout():
    print("AHHHH")
    await asyncio.sleep(2)
    print("I did")
async def response():       
    print("who the hell said that?")
    await asyncio.sleep(2.5)    
    print("oh alright")

async def main():
    await asyncio.gather(shout(),response())
   
asyncio.run(main())
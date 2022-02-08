import asyncio
import websockets


async def handler(websocket):
    # while True:
    #     try:
    #         message = await websocket.recv()
    #     except websockets.ConnectionClosedOK:
    #         break
    #     print(message)
    #     the above pattern of waiting on a message and handling a closed connection is so common that
    #     there is a shorter way to do it
    async for message in websocket:
        print(message)


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())

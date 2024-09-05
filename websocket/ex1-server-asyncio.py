#!/usr/bin/env python

import asyncio
from websockets.asyncio.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def manipulador(canal):
    async for mensagem in canal:
        print(mensagem)

async def main():
    async with serve(manipulador, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())
#!/usr/bin/env python

import asyncio, json, itertools
from connect4 import PLAYER1, PLAYER2, Connect4

from websockets.asyncio.server import serve


async def manipulador(websocket):
    game = Connect4()

    turns = itertools.cycle([PLAYER1, PLAYER2])
    player = next(turns)

    async for mensagem in websocket:

        event = json.loads(mensagem)
        print(event)
        assert event["type"] == "play"
        column = event["column"]

        try:
            row = game.play(player, column)
        except ValueError as exc:
            event = {
                "type": "error",
                "message": str(exc)
            }
            await websocket.send(json.dumps(event))
            continue
        event = {

            "type": "play",

            "player": player,

            "column": column,

            "row": row,

        }

        await websocket.send(json.dumps(event))


        # If move is winning, send a "win" event.

        if game.winner is not None:

            event = {

                "type": "win",

                "player": game.winner,

            }

            await websocket.send(json.dumps(event))


        # Alternate turns.

        player = next(turns)

async def main():
    async with serve(manipulador, "", 8001):
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
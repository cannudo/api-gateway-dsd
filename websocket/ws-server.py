#!/usr/bin/env python

import asyncio
from websockets.asyncio.server import serve

# Armazenar todos os canais de clientes conectados
clientes_conectados = set()

async def manipulador(canal):
    # Adicionar o cliente à lista de clientes conectados
    clientes_conectados.add(canal)
    try:
        async for mensagem in canal:
            print(mensagem)
            # Enviar a mensagem recebida para todos os clientes conectados
            await asyncio.gather(*[cliente.send(mensagem) for cliente in clientes_conectados])
    except:
        pass
    finally:
        # Remover o cliente da lista quando a conexão for fechada
        clientes_conectados.remove(canal)

async def main():
    async with serve(manipulador, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())

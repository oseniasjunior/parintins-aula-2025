import asyncio
import websockets

async def test_ws():
    uri = "ws://127.0.0.1:8001/sale_channel/"
    async with websockets.connect(uri) as ws:
        print("✅ Conectado ao WebSocket!")
        await ws.send("hello world")
        resposta = await ws.recv()
        print("📩 Recebido:", resposta)

asyncio.run(test_ws())

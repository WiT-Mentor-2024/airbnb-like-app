import asyncio
import websockets


async def test_websocket():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket")

        # Отправляем начальное сообщение
        await websocket.send("Hello")

        try:
            while True:
                message = await websocket.recv()
                print(f"Received: {message}")
        except websockets.ConnectionClosed:
            print("Connection closed")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test_websocket())

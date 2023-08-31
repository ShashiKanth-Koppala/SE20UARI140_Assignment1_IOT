import asyncio
import websockets

async def communicate_with_server():
    try:
        url = "ws://139.59.33.235:5001"
        async with websockets.connect(url) as ws_connection:
            client_message = "Hello from client, John Doe."
            await ws_connection.send(client_message)
            print(f"transmitted to server:: {client_message}")

            response = await ws_connection.recv()
            print(f"Server responded: {response}")
    except websockets.exceptions.ConnectionClosed:
        print("Lost connection to server.")

async def main():
    await communicate_with_server()

asyncio.run(main())
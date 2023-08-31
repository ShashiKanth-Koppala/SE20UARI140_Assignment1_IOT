import asyncio
import websockets

async def interact_with_remote(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            response = f"Server: Hi client this is the server!"
            await websocket.send(response)
            print(f"Sent message to client: {response}")
    except websockets.exceptions.ConnectionClosed:
        print("Disconnected from remote.")

async def main():
    async with websockets.serve(interact_with_remote, "139.59.33.235", 5001):
        print(f"server active")
        await asyncio.Future()
        
if __name__ == "__main__":
    asyncio.run(main())
import asyncio
import websockets
from websockets import ClientConnection

async def chat() -> None:
    uri: str = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        ws: ClientConnection = websocket
        print("Connected to server. Type messages to send. Type 'exit' to quit.")

        while True:
            message: str = input("> ")

            if message.lower() == "exit":
                print("Closing connection...")
                break

            await ws.send(message)
            print(f"Sent: {message}")

            response: str = await ws.recv()
            print(f"Received: {response}")
            if response == "Server echo: Connection Closed":
                print("Closing connection...")
                break

if __name__ == "__main__":
    try:
        asyncio.run(chat())
    except KeyboardInterrupt:
        print("\nClient terminated by user.")

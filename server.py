import asyncio
import websockets
from websockets import ClientConnection


class Server:
    clients = []

    async def add_client(self, client: tuple):
        self.clients.append(client)
        print(f"[SERVER] Total clients: {len(self.clients)}")

    async def remove_client(self, client: tuple):
        self.clients.remove(client)
        print(f"[SERVER] Total clients: {len(self.clients)}")

    async def handle_client(self, websocket: ClientConnection) -> None:
        print(f"Client connected: {websocket.remote_address}")
        await self.add_client(websocket.remote_address)

        try:
            async for message in websocket:
                print(f"Received: {message}")
                await websocket.send(f"Server echo: {message}")
        except websockets.ConnectionClosed as e:
            await self.remove_client(websocket)
            websocket.send(f"Server echo: Connection Closed")
            print(f"Client disconnected. Reason: {e}")

    async def run(self) -> None:
        async with websockets.serve(self.handle_client, "0.0.0.0", 8765):
            print("WebSocket server started on ws://0.0.0.0:8765")
            await asyncio.Future()  # run forever

    
if __name__ == "__main__":

    server = Server()
    asyncio.run(server.run())

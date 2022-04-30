import websockets
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient

ws_client = WebsocketClient(stream_url='wss://testnet.binance.vision')
# import asyncio
#
# async def main():
#     url = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"
#     async with websockets.connect(url) as client:
#         print(await client.recv())
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient

def message_handler(message):
    print(message)

ws_client = WebsocketClient()
ws_client.start()

ws_client.mini_ticker(
    symbol='bnbusdt',
    id=1,
    callback=message_handler,
)

# Combine selected streams
ws_client.instant_subscribe(
    stream=['bnbusdt@bookTicker', 'ethusdt@bookTicker'],
    callback=message_handler,
)

ws_client.stop()
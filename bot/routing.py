from channels.routing import route
from index.consumers import ws_disconnect, ws_connect, ws_receive

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_receive),
    route("websocket.disconnect", ws_disconnect),
]

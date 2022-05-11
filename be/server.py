import asyncio
import uvicorn
import sys
from app import BigApp
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute, Route
from starlette.responses import JSONResponse

app: BigApp = None

async def create_app():
    global app
    try:
        if app is None:
            app = BigApp()
    except Exception as e:
        raise RuntimeError("Error creating BE app.") from e

def remove_app():
    global app
    app = None

async def server_ready(request):
    global app
    return JSONResponse({"ready": app is not None})

class Server(WebSocketEndpoint):
    def process_request(self, websocket, request):
        if not request:
            trace = sys._getframe(1).f_code.co_name
            raise RuntimeError(f"Empty json request msg. Trace: {trace}")
        else:
            global app
            app.process_request(request)

    async def on_connect(self, websocket):
        global app
        callback = self.create_client_callback(websocket)
        self.callback = callback
        self.client_id = app.register_client(callback)
        await websocket.accept()

    async def on_disconnect(self, websocket, close_code):
        global app
        app.unregister_client(self.client_id)
        return await super().on_disconnect(websocket, close_code)

    async def on_receive(self, websocket, request):
        self.process_request(websocket, request)

    def create_client_callback(self, websocket):
        async def client_callback(response):
            if not isinstance(response, list):
                response = [response]
            for r in response:
                try:
                    await websocket.send_json(r)
                except Exception as e:
                    raise RuntimeError("Error sending JSON response") from e

        return client_callback

routes = [
    WebSocketRoute("/appserver", endpoint=Server),
    Route("/isready", endpoint=server_ready)
]

_app = Starlette(
    routes=routes,
    on_startup=[create_app],
    on_shutdown=[remove_app]
)

_default_host = "0.0.0.0"
_default_port = 8000

def main(host = _default_host, port = _default_port):
    uvicorn.run(_app, host=host, port=port)


if __name__ == "__main__":
    main()


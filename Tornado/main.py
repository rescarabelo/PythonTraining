from abc import ABC
from typing import Union, Optional, Awaitable

import tornado.ioloop
import tornado.web
import tornado.websocket


class WebSocket(tornado.websocket.WebSocketHandler, ABC):
    def check_origin(self, origin: str) -> bool:
        return True

    def open(self):
        print("WebSocket connected.")

    def on_message(self, message: Union[str, bytes]) -> Optional[Awaitable[None]]:
        self.write_message(u"You said: " + message)

    def on_close(self) -> None:
        print("Closing WebSocket...")


class BasicRequestHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write("Hello World!")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/websocket", WebSocket),
        (r"/", BasicRequestHandler)
    ])
    app.listen(8888)
    print("listening on port 8888")
    tornado.ioloop.IOLoop.instance().start()

from typing import Any, Dict

import arrow
import requests
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class CurrentTimeHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self) -> None:
        utc = arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")
        self.write({"message": f"{utc}"})


class RecommendationsHandler(RequestHandler):
    def post(self) -> None:
        api_key: str = "f53dd4aea5bfc8ecd850fcbe1b08921e"
        url: str = "https://news-api.lateral.io/documents/similar-to-text"
        payload: str = '{"text": "machine learning is" }'
        headers: Dict[str, Any] = {
            "subscription-key": f"{api_key}",
            "content-type": "application/json",
        }
        response = requests.request("POST", url, data=payload, headers=headers)

        self.write({"message": f"{response.text}"})


def make_app() -> Application:
    urls: Any = [
        ("/", CurrentTimeHandler),
        ("/recommendations", RecommendationsHandler),
    ]
    return Application(urls, debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    IOLoop.instance().start()

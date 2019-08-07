from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import arrow


class HelloHandler(RequestHandler):
    def get(self):
        utc = arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")
        self.write({'message': f'{utc}'})


def make_app():
    urls = [("/", HelloHandler)]
    return Application(urls)


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    IOLoop.instance().start()
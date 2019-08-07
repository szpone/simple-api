import tornado.ioloop
from tornado.httpclient import HTTPRequest
from tornado.testing import AsyncHTTPTestCase, gen_test
import api


class APITest(AsyncHTTPTestCase):
    def get_app(self):
        return api.make_app()

    def get_new_ioloop(self):
        return tornado.ioloop.IOLoop.instance()

    @gen_test
    def test_bad_request(self):
        request = HTTPRequest(url=self.get_url('/'))
        response = yield self.http_client.fetch(request)
        self.assertEqual(response.code, 200)
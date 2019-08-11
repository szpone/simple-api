import json

from tornado.testing import AsyncHTTPTestCase

import api


class APITest(AsyncHTTPTestCase):
    def get_app(self):
        return api.make_app()

    def test_homepage(self):
        response = self.fetch("/")
        self.assertEqual(response.code, 200)

    def test_recommendations(self):
        response = self.fetch(
            "/recommendations",
            method="POST",
            body=json.dumps({"text": "machine learning is a"}),
            headers={
                "Content-Type": "application/json",
                "subscription-key": "f53dd4aea5bfc8ecd850fcbe1b08921e",
            },
        )
        self.assertEqual(response.code, 200)

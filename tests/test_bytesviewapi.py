import os
from bytesviewapi import BytesviewApiClient 
import unittest

class test_bytesviwapi(unittest.TestCase):
    def setUp(self):
        # your private API key.
        key = os.environ.get("TOKEN")
        self.api = BytesviewApiClient(key)

    def test_sentiment_api(self):
        response = self.api.sentiment_api(data = {0: "this is good"}, lang = "en")

        self.assertEqual(str(list(response.keys())[0]), str(0))



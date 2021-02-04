import os
from bytesviewapi.bytesviewapi_client import BytesviewapiClient 
import unittest

class test_bytesviwapi(unittest.TestCase):
    def setUp(self):
        #key = os.environ.get("x-access-token")
        key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im5hbXJhdGFAYWxnb2RvbW1lZGlhLmNvbSJ9.ceDtxy7gbSSI1t3lrokTBMNajge7oPrmo07R7phKRI8"
        self.api = BytesviewapiClient(key)

    def test_sentiment_api(self):

        '''

        # Raise TypeError if Keyword/Phrase param is not of type str
        q = 0
        with self.assertRaises(TypeError):
            self.api.sentiment_api(data = {0: "this is good"}, lang = "en")
        '''
        #print(self.api.sentiment_api(data = {0: "this is good"}, lang = "at"))
        assert self.api.sentiment_api(data = {0: "this is good"}, lang = "en")

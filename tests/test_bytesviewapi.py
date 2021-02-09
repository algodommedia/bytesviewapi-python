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

        self.assertEqual(str(list(response.keys())[0]), "0")

    def test_emotion_api(self):
        response = self.api.emotion_api(data = {0: "this is good"}, lang = "en")

        self.assertEqual(str(list(response.keys())[0]), "0")

    def test_keywords_api(self):
        response = self.api.keywords_api(data = {0: "this is good"}, lang = "en")

        self.assertEqual(str(list(response.keys())[0]), "0")

    def test_semantic_api(self):
        response = self.api.semantic_api(data = {"string1": "this is good", "string2": "this is good"}, lang = "en")
        
        self.assertEqual(str(list(response.keys())[0]), "score")

    def test_name_gender_api(self):
        response = self.api.name_gender_api(data = {0: "ron"})
        
        self.assertEqual(str(list(response.keys())[0]), "0")

    def test_ner_api(self):
        response = self.api.ner_api(data = {0: "this is good"}, lang = "en")
        
        self.assertEqual(str(list(response.keys())[0]), "0")
    
    def test_intent_api(self):
        response = self.api.intent_api(data = {0: "this is good"}, lang = "en")
        
        self.assertEqual(str(list(response.keys())[0]), "0")
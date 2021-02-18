import os
from bytesviewapi import BytesviewApiClient 
import unittest

class test_bytesviwapi(unittest.TestCase):
    def setUp(self):
        # your private API key.
        key = os.environ.get("PYTEST_TOKEN")
        self.api = BytesviewApiClient(key)

    def test_sentiment_api(self):
        response = self.api.sentiment_api(data = {"key1": "this is my favourite food"}, lang = "en")

        self.assertEqual(response['success']['key1']['label'], 2)

    def test_emotion_api(self):
        response = self.api.emotion_api(data = {"key1": "this is good"}, lang = "en")

        self.assertEqual(response['success']['key1']['label'], 2)

    def test_keywords_api(self):
        response = self.api.keywords_api(data = {"key1": "Apple hasn't announced the tracking fobs"}, lang = "en")

        self.assertEqual(str(response['success']['key1']['tags'][0]), "Apple")

    def test_semantic_api(self):
        response = self.api.semantic_api(data = {"string1": "this is good", "string2": "this is good"}, lang = "en")
        
        self.assertEqual(response['success']['score'], 100)
        

    def test_name_gender_api(self):
        response = self.api.name_gender_api(data = {"key1": "ron"})
        
        self.assertEqual(str(response['success']['key1']['gender']), "M")

    def test_ner_api(self):
        response = self.api.ner_api(data = {"key1": "Mauritania and the IMF agreed Poverty Reduction arrangement"}, lang = "en")
        self.assertEqual(str(response['success']['key1']['name'][0]), 'Mauritania')
    
    def test_intent_api(self):
        response = self.api.intent_api(data = {"key1": "please subscribe to our channel"}, lang = "en")
        
        self.assertEqual(response['success']['key1']['label'], 2)

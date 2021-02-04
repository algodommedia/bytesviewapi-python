
import requests
from bytesviewapi.api_authentication import BytesApiAuth
from bytesviewapi import env_file
from bytesviewapi.utils import is_valid_json, is_valid_dict
import json
from bytesviewapi.bytesviewapi_exception import BytesviewException

class BytesviewapiClient(object):

    def __init__(self, api_key, session=None):
        self.header = BytesApiAuth(api_key=api_key)
        if session is None:
            self.request_method = requests
        else:
            self.request_method = session

    def sentiment_api( self, data=None, lang="en"):
        
        payload = {}

        # Keyword/Phrase
        if data is not None:
            if is_valid_dict(data):
                payload["data"] = data
            else:
                raise TypeError("Data should be of type dictionary")
        else:
            raise ValueError("Please provide data, data can not be empty")

        # check if valid language string
        if isinstance(lang, str):
            if lang in env_file.sentiment_languages_support:
                payload["lang"] = lang
            else:
                raise ValueError("Please provide valid Language code, check documentation for supported languages")
        else:
            raise TypeError("Language input should be an string")
        
        # Send Request
        response = self.request_method.post(env_file.SENTIMENT_URL, auth=self.header, timeout=300, data=json.dumps(payload, indent = 4)) 

        # Check Status of Request
        if response.status_code != 200:
            raise BytesviewException(response.json())

        return response.json()







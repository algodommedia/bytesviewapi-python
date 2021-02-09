import requests
from bytesviewapi.api_authentication import BytesApiAuth
from bytesviewapi import env_file
from bytesviewapi.utils import is_valid_dict
import json
from bytesviewapi.bytesviewapi_exception import BytesviewException

class BytesviewApiClient(object):

    def __init__(self, api_key=None, session=None):

        """ Initializes Byteview client object for access Bytesview APIs """
        
        """
        :param api_key: your API key.
        :type api_key:  string
        :param session: Default value for this argument is None but if you’re making several requests to the same host, 
                        the underlying TCP connection will be reused, which can result in a significant performance increase. 
                        Please make sure call session.close() after execute all calls to free up resource.   
        :type session: requests.Session
        """        
        
        self.api_key = api_key
        # BytesviewAPI request header 
        self.header = BytesApiAuth(api_key=self.api_key)
        # Check if session argument is None 
        if session is None:
            self.request_method = requests
        else:
            self.request_method = session


    def sentiment_api( self, data=None, lang="en"):
        """ Sending POST request to the sentiment api"""
        
        """
        :param data: pass your desired strings in the dictionary format where each string has some unique key. (ex. {0: "this is good"})
        :type data: dictionary
        :param lang: Language Code (English - en, Arabic - ar), Default laguage is english(en) 
        :type data: string
        :return: server response in JSON object 
        """
        
        payload = {}

        if self.api_key is None:
            raise ValueError("Please provide your private API Key")

        # Check if valid data dictionary
        if data is not None:
            if is_valid_dict(data):
                payload["data"] = data
            else:
                raise TypeError("Data should be of type dictionary")
        else:
            raise ValueError("Please provide data, data can not be empty")

        # Check if valid language string
        if isinstance(lang, str):
            if lang in env_file.sentiment_languages_support:
                payload["lang"] = lang
            else:
                raise ValueError("Please provide valid Language code, check documentation for supported languages")
        else:
            raise TypeError("Language input should be an string")
        

        # Make a POST request to env_file.SENTIMENT_URL
        response = self.request_method.post(env_file.SENTIMENT_URL, auth=self.header, timeout=300, data=json.dumps(payload, indent = 4)) 


        # Check the status code of the response if not equal to 200, then raise exception
        if response.status_code != 200:
            raise BytesviewException(response.json())
        
        # Return the response json
        return response.json()
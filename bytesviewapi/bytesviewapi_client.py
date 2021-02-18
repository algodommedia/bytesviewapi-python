import requests
from bytesviewapi.api_authentication import BytesApiAuth
from bytesviewapi import constants
from bytesviewapi.utils import is_valid_dict
import json
from bytesviewapi.bytesviewapi_exception import BytesviewException
from bytesviewapi.helpers import post, MaxRetries


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
        
        # Default value for maximum retries and retry delay is zero 
        self.max_retries = 0
        self.retry_delay = 0

        # Default proxies value is none
        self.proxies = None

        # set request timeout
        self.request_timeout = constants.DEFAULT_REQUEST_TIMEOUT

    def set_retries( self, max_retries=0, retry_delay = 0):
        """ API maximum retry and delay when getting 500 error """
        
        """
        :param max_retries: Your maximum retries when server responding with 500 internal error, Default value for this augument is zero.
        :type max_retries:  integer 
        :param retry_delay: Delay(in seconds) between retries when server responding with 500 error, Default value for this augument 
                            is zero seconds.
        :type retry_delay:  integer
        """
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def set_request_timeout( self, request_timeout = constants.DEFAULT_REQUEST_TIMEOUT):
        """ API maximum timeout for the request """
        
        """
        :param request_timeout: How many seconds to wait for the client to make a connection and/or send a response.
        :type request_timeout:  integer 
        """
        self.request_timeout = request_timeout

    def api_proxies( self, proxies):
        """ Configure Proxie dictionary """
        
        """
        :param proxies: A dictionary of the protocol to the proxy url ( ex.{ "https" : "https://1.1.1.1:80"}).
        :type proxies:  dictionary 
        """
        self.proxies = proxies

    def sentiment_api( self, data=None, lang="en"):
        """ Sending POST request to the sentiment api"""
        
        """
        :param data: pass your desired strings in the dictionary format where each string has some unique key. (ex. {0: "this is good"})
        :type data: dictionary
        :param lang: Language Code (English - en, Arabic - ar, Japanese = ja, Turkish = tr), Default laguage is english(en) 
        :type lang: string
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
            if lang in constants.SENTIMENT_LANGUAGES_SUPPORT:
                payload["lang"] = lang
            else:
                raise ValueError("Please provide valid Language code, check documentation for supported languages")
        else:
            raise TypeError("Language input should be an string")
        

        # Make a POST request to constants.SENTIMENT_URL 
        response = post(self.request_method,  constants.SENTIMENT_URL, self.header, payload, self.proxies, self.request_timeout)
        
        if response.status_code == 500:
            response = MaxRetries(response, self.max_retries, self.retry_delay, self.request_method, constants.SENTIMENT_URL, self.header, payload, self.proxies, self.request_timeout)

        # Check the status code of the response if not equal to 200, then raise exception
        if response.status_code != 200:
            raise BytesviewException(response.json())
        
        # Return the response json
        return response.json()


    def emotion_api( self, data=None, lang="en"):
        """ Sending POST request to the emotion api"""
        
        """
        :param data: pass your desired strings in the dictionary format where each string has some unique key. (ex. {0: "this is good"})
        :type data: dictionary
        :param lang: Language Code (English - en), Default laguage is english(en) 
        :type lang: string
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
            if lang in constants.EMOTION_LANGUAGES_SUPPORT:
                payload["lang"] = lang
            else:
                raise ValueError("Please provide valid Language code, check documentation for supported languages")
        else:
            raise TypeError("Language input should be an string")
        

        # Make a POST request to constants.EMOTION_URL
        response = post(self.request_method,  constants.EMOTION_URL, self.header, payload, self.proxies, self.request_timeout)
        
        if response.status_code == 500:
            response = MaxRetries(response, self.max_retries, self.retry_delay, self.request_method, constants.EMOTION_URL, self.header, payload, self.proxies, self.request_timeout) 


        # Check the status code of the response if not equal to 200, then raise exception
        if response.status_code != 200:
            raise BytesviewException(response.json())
        
        # Return the response json
        return response.json()

    def keywords_api( self, data=None, lang="en"):
        """ Sending POST request to the keywords api"""
        
        """
        :param data: pass your desired strings in the dictionary format where each string has some unique key. (ex. {0: "this is good"})
        :type data: dictionary
        :param lang: Language Code (English - en), Default laguage is english(en) 
        :type lang: string
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
            if lang in constants.KEYWORDS_LANGUAGES_SUPPORT:
                payload["lang"] = lang
            else:
                raise ValueError("Please provide valid Language code, check documentation for supported languages")
        else:
            raise TypeError("Language input should be an string")
        

        # Make a POST request to constants.KEYWORDS_URL
        response = post(self.request_method,  constants.KEYWORDS_URL, self.header, payload, self.proxies, self.request_timeout)
        
        if response.status_code == 500:
            response = MaxRetries(response, self.max_retries, self.retry_delay, self.request_method, constants.KEYWORDS_URL, self.header, payload, self.proxies, self.request_timeout) 


        # Check the status code of the response if not equal to 200, then raise exception
        if response.status_code != 200:
            raise BytesviewException(response.json())
        
        # Return the response json
        return response.json()


    def semantic_api( self, data=None, lang="en"):
        """ Sending POST request to the semantic api"""
        
        """
        :param data: Pass your both strings in the unique keys of the dictionary. (ex. {"string1": "this is good", "string2": "this is great"})
        :type data: dictionary
        :param lang: Language Code (English - en), Default laguage is english(en) 
        :type lang: string
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
            if lang in constants.SEMANTIC_LANGUAGES_SUPPORT:
                payload["lang"] = lang
            else:
                raise ValueError("Please provide valid Language code, check documentation for supported languages")
        else:
            raise TypeError("Language input should be an string")
        

        # Make a POST request to constants.SEMANTIC_URL
        response = post(self.request_method,  constants.SEMANTIC_URL, self.header, payload, self.proxies, self.request_timeout)
        
        if response.status_code == 500:
            response = MaxRetries(response, self.max_retries, self.retry_delay, self.request_method, constants.SEMANTIC_URL, self.header, payload, self.proxies, self.request_timeout)


        # Check the status code of the response if not equal to 200, then raise exception
        if response.status_code != 200:
            raise BytesviewException(response.json())
        
        # Return the response json
        return response.json()


    def name_gender_api( self, data=None):
        """ Sending POST request to the name-gender api"""
        
        """
        :param data: Pass your desired names in the dictionary format where each string has some unique key. (ex. {0: "ron"})
        :type data: dictionary
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

        # Make a POST request to constants.NAME_GENDER_URL
        response = post(self.request_method,  constants.NAME_GENDER_URL, self.header, payload, self.proxies, self.request_timeout)
        
        if response.status_code == 500:
            response = MaxRetries(response, self.max_retries, self.retry_delay, self.request_method, constants.NAME_GENDER_URL, self.header, payload, self.proxies, self.request_timeout)


        # Check the status code of the response if not equal to 200, then raise exception
        if response.status_code != 200:
            raise BytesviewException(response.json())
        
        # Return the response json
        return response.json()


    def ner_api( self, data=None, lang="en"):
        """ Sending POST request to the ner api"""
        
        """
        :param data: pass your desired strings in the dictionary format where each string has some unique key. (ex. {0: "this is good"})
        :type data: dictionary
        :param lang: Language Code (English - en), Default laguage is english(en) 
        :type lang: string
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
            if lang in constants.NER_LANGUAGES_SUPPORT:
                payload["lang"] = lang
            else:
                raise ValueError("Please provide valid Language code, check documentation for supported languages")
        else:
            raise TypeError("Language input should be an string")
        

        # Make a POST request to constants.NER_URL
        response = post(self.request_method,  constants.NER_URL, self.header, payload, self.proxies, self.request_timeout)
        
        if response.status_code == 500:
            response = MaxRetries(response, self.max_retries, self.retry_delay, self.request_method, constants.NER_URL, self.header, payload, self.proxies, self.request_timeout)


        # Check the status code of the response if not equal to 200, then raise exception
        if response.status_code != 200:
            raise BytesviewException(response.json())
        
        # Return the response json
        return response.json()


    def intent_api( self, data=None, lang="en"):
        """ Sending POST request to the intent api"""
        
        """
        :param data: pass your desired strings in the dictionary format where each string has some unique key. (ex. {0: "this is good"})
        :type data: dictionary
        :param lang: Language Code (English - en), Default laguage is english(en) 
        :type lang: string
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
            if lang in constants.INTENT_LANGUAGES_SUPPORT:
                payload["lang"] = lang
            else:
                raise ValueError("Please provide valid Language code, check documentation for supported languages")
        else:
            raise TypeError("Language input should be an string")
        

        # Make a POST request to constants.INTENT_URL
        response = post(self.request_method,  constants.INTENT_URL, self.header, payload, self.proxies, self.request_timeout)
        
        if response.status_code == 500:
            response = MaxRetries(response, self.max_retries, self.retry_delay, self.request_method, constants.INTENT_URL, self.header, payload, self.proxies, self.request_timeout) 


        # Check the status code of the response if not equal to 200, then raise exception
        if response.status_code != 200:
            raise BytesviewException(response.json())
        
        # Return the response json
        return response.json()
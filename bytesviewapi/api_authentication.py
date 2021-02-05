from requests.auth import AuthBase


class BytesApiAuth(AuthBase):
    """ BytesviewApi authorization header update """

    """
    :param api_key: your API key.
    :type api_key:  string
    """
    
    def __init__(self, api_key):
        self.api_key = api_key
    

    def __call__(self, request):
        request.headers.update(api_headers(self.api_key))
        return request


def api_headers(api_key):
    """ Return API request header"""
    return {
        "Content-Type": "Application/JSON", 
        "x-access-token": api_key
        }



    
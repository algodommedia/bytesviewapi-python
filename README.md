# Bytesviewapi Python Client
Bytesviewapi allows you to create a library for accessing http services easily, in a centralized way. An API defined by bytesviewapi will return a JSON object when called.

# Installation

## Supported Python Versions
Python >= 3.5 fully supported and tested.

## Install Package
```
pip install bytesviewapi
```
## Quick Start

`POST 1/static/sentiment`

```
from bytesviewapi import BytesviewapiClient

# API key authorization, Initialize the client with your API key:
api = BytesviewapiClient(api_key="API key")

# pass your desired strings in a dictionary with unique key
data = {"key1": "We are good here", "key2": "this is not what we expect"}

response = api.sentiment_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your desired strings in the dictionary format where each string has some unique key. 

`lang` : Language Code (English - en, Arabic - ar), Default laguage is english(en).

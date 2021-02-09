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


### SENTIMENT API

`POST 1/static/sentiment`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your desired strings in a dictionary with unique key
data = {"key1": "We are good here", "key2": "this is not what we expect"}

response = api.sentiment_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your desired strings in the dictionary format where each string has some unique key. 

`lang` : Language Code (English - en, Arabic - ar), Default language is english(en).

&nbsp;
### EMOTION API

`POST 1/static/emotion`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your desired strings in a dictionary with unique key
data = {"key1": "I am not feeling good", "key2": "happy that you come here"}

response = api.emotion_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your desired strings in the dictionary format where each string has some unique key. 

`lang` : Language Code (English - en), Default language is english(en).

&nbsp;
### KEYWORDS API

`POST 1/static/keywords`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your desired strings in a dictionary with unique key
data = {"key1": "Accessories for AirTags appearing online, Apple hasn't announced the tracking fobs"}

response = api.keywords_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your desired strings in the dictionary format where each string has some unique key. 

`lang` : Language Code (English - en), Default language is english(en).

&nbsp;
### SEMANTIC API

`POST 1/static/semantic`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your both strings in the "string1" and "string2" key of the dictionary
data = {"string1": "A smiling costumed woman is holding an umbrella.", "string2": "A happy woman in a fairy costume holds an umbrella."}
response = api.semantic_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your both strings in the "string1" and "string2" key of the dictionary. 

`lang` : Language Code (English - en), Default language is english(en).

&nbsp;
### NAME-GENDER API

`POST 1/static/name-gender`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your desired names in the dictionary format where each string has some unique key.
data ={"key1":"alvina", "key2":"نسترن", "key3":"ron", "key4":"rinki", "key5":"オウガ"}
response = api.name_gender_api(data = data)

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your desired names in the dictionary format where each string has some unique key.

&nbsp;
### NAMED-ENTITY API

`POST 1/static/ner`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your desired strings in a dictionary with unique key
data = {"key1":"Mauritania and the IMF agreed Poverty Reduction arrangement"}
response = api.ner_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your desired strings in the dictionary format where each string has some unique key. 

`lang` : Language Code (English - en), Default language is english(en).

&nbsp;
### INTENT API

`POST 1/static/intent`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your desired strings in a dictionary with unique key
data = {"key1":"Adam Rippon Wins 'Dancing With The Stars' Because It Was Destined"}
response = api.intent_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your desired strings in the dictionary format where each string has some unique key. 

`lang` : Language Code (English - en), Default language is english(en).
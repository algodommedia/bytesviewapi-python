![Alt text](https://raw.githubusercontent.com/algodommedia/bytesviewapi-python/main/bytesview-logo.png)

# <p align="center">Bytesviewapi Python Client
Bytesviewapi allows you to create a library for accessing http services easily, in a centralized way. An API defined by bytesviewapi will return a JSON object when called.

[![Build Status](https://img.shields.io/github/workflow/status/algodommedia/bytesviewapi-python/Upload%20Python%20Package)](https://github.com/algodommedia/bytesviewapi-python/actions?query=workflow%3A%22Upload+Python+Package%22)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/algodommedia/bytesviewapi-python/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/bytesviewapi?color=fd7e14)](https://pypi.org/project/bytesviewapi)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pyTelegramBotAPI.svg)](https://pypi.org/project/bytesviewapi)
[![Python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://pypi.org/project/bytesviewapi)

<br />

# Installation

## Supported Python Versions
Python >= 3.5 fully supported and tested.

## Install Package
```
pip install bytesviewapi
```

## Quick Start

Bytesviewapi docs can be seen [here](https://www.bytesview.com/docs/).

<br />

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

`lang` : Pass [ISO code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the following supported language `English`, `Arabic`, `Turkish`, `Japanese`, `Spanish`, `French`, `German`, `Russian`, `Chinese(simplified)`, `Swedish`, `Czech`, `Danish`, `Greek`, `Korean`, `Latin`, `Hebrew`, `Indonesian`, `Kazakh`, `Armenian`, `Azerbaijani`, `Belarussian`, `Finnish`, `Bulgarian`, `Burmese`, `Persian`, `Portuguese`, `Urdu`, `Vietnamese`, `Thai`, `Hungarian`, `Italian`, `Polish`, `Ukrainian`, `Uzbek`. The default language is english(en).

<br />

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

`lang` : Pass [ISO code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the following supported language `English`, `Arabic`, `Turkish`, `Japanese`, `Spanish`, `French`, `German`, `Russian`, `Chinese(simplified)`, `Swedish`, `Czech`, `Danish`, `Greek`, `Korean`, `Latin`, `Hebrew`, `Indonesian`, `Kazakh`, `Armenian`, `Azerbaijani`, `Belarussian`, `Finnish`, `Bulgarian`, `Burmese`, `Persian`, `Portuguese`, `Urdu`, `Vietnamese`, `Thai`, `Hungarian`, `Italian`, `Polish`, `Ukrainian`, `Uzbek`. The default language is english(en). 

<br />

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

`lang` : Pass [ISO code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the following supported language `English`, `French`, `Turkish`, `German`, `Japanese`, `Chinese(simplified)`, `Spanish`, `Arabic`, `Russian`, `Italian`, `Danish`. The default language is english(en).

<br />

### SEMANTIC API

`POST 1/static/semantic`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your both strings in the dictionary format with some unique key
data = {"string1": "A smiling costumed woman is holding an umbrella.", "string2": "A happy woman in a fairy costume holds an umbrella."}

response = api.semantic_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your both strings in the dictionary format with some unique key. 

`lang` : Language Code (English - en), Default language is english(en).

<br />

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

<br />

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

<br />

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

<br />

### FEATURE API

`POST 1/static/feature`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your desired strings in a dictionary with unique key
data = {"key1":"This is probably one of the funniest films of the 1980's. Eddie Murphy does a fine job as con man Billy Ray and Dan Ackroyd is great as Louis."}

response = api.feature_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your desired strings in the dictionary format where each string has some unique key. 

`lang` : Language Code (English - en), Default language is english(en).

<br />

### TOPIC API

`POST 1/static/topic`

```
from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key="API key")

# Pass your desired strings in a dictionary with unique key
data = {"key1":"Shriram Automall India Limited is hiring for Accounts Department."}

response = api.topic_api(data = data , lang = "en")

```
`API key` : Your private Bytesview API key. 

`data` : You can pass your desired strings in the dictionary format where each string has some unique key. 

`lang` : Language Code (English - en), Default language is english(en).
<br />

## License

Provided under [MIT License](https://github.com/algodommedia/bytesviewapi-python/blob/main/LICENSE) by Matt Lisivick.

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
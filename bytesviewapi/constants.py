# All the API URL and language suported by API.
BASE_URL = 'https://api.bytesview.com/1/'

# Sentiment URL 
SENTIMENT_URL = BASE_URL + 'static/sentiment'
SENTIMENT_LANGUAGES_SUPPORT = {"ar", "en", 'ja', 'tr', 'hy', 'az', 'be', 'fi', 'bg', 'my', 'zh', 'cs', 'da', 'fr', 'de', 'el',
                               'he', 'id', 'kk', 'ko', 'la', 'pa', 'pt', 'ru', 'es', 'sv', 'ur', 'vi', 'th', 'hu', 'it', 'pl',
                               'uk', 'uz'}


# Emotion URL 
EMOTION_URL = BASE_URL + 'static/emotion'
EMOTION_LANGUAGES_SUPPORT = {"ar", "en", 'ja', 'tr', 'hy', 'az', 'be', 'fi', 'bg', 'my', 'zh', 'cs', 'da', 'fr', 'de', 'el',
                            'he', 'id', 'kk', 'ko', 'la', 'pa', 'pt', 'ru', 'es', 'sv', 'ur', 'vi', 'th', 'hu', 'it', 'pl',
                            'uk', 'uz'}


# Keywords URL 
KEYWORDS_URL = BASE_URL + 'static/keywords'
KEYWORDS_LANGUAGES_SUPPORT = {'en', 'fr', 'de', 'da', 'it', 'es', 'zh', "ja", "ru", "tr", "ar"}


# Semantic URL 
SEMANTIC_URL = BASE_URL + 'static/semantic'
SEMANTIC_LANGUAGES_SUPPORT = {"en"}


# Name-gender URL 
NAME_GENDER_URL = BASE_URL + 'static/name-gender'


# NER URL 
NER_URL = BASE_URL + 'static/ner'
NER_LANGUAGES_SUPPORT = {"en"}


# Intent URL 
INTENT_URL = BASE_URL + 'static/intent'
INTENT_LANGUAGES_SUPPORT = {"en"}

# Default request timeout is 300 seconds 
DEFAULT_REQUEST_TIMEOUT = 300
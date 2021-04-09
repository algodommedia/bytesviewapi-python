from bytesviewapi import BytesviewApiClient

# API key authorization, Initialize the client with your API key
api = BytesviewApiClient(api_key='API Key')

# Sentiment API
response = api.sentiment_api(data = {"key1": "we are good here"}, lang = "en")
print(response)

# Emotion API
response = api.emotion_api(data = {"key1": "I am not feeling good"}, lang = "en")
print(response)

# Keywords API
response = api.keywords_api(data = {"key1": "Accessories for AirTags appearing online, Apple hasn't announced the tracking fobs"}, lang = "en")
print(response)

# Semantic API
response = api.semantic_api(data = {"string1": "A smiling costumed woman is holding an umbrella.", "string2": "A happy woman in a fairy costume holds an umbrella."}, lang = "en")
print(response)

# Name-gender API
response = api.name_gender_api(data = {"key1":"alvina", "key2":"نسترن", "key3":"ron", "key4":"rinki", "key5":"オウガ"})
print(response)

# Named-entity API
response = api.ner_api(data = {"key1":"Mauritania and the IMF agreed Poverty Reduction arrangement"}, lang = "en")
print(response)

# Intent API
response = api.intent_api(data = {"key1":"Adam Rippon Wins 'Dancing With The Stars' Because It Was Destined"}, lang = "en")
print(response)

# Feature API
data = {"key1":"This is probably one of the funniest films of the 1980's. Eddie Murphy does a fine job as con man Billy Ray and Dan Ackroyd is great as Louis."}
response = api.feature_api(data = data , lang = "en")
print(response)

# Topic API
response = api.topic_api(data = {"key1":"Shriram Automall India Limited is hiring for Accounts Department."} , lang = "en")
print(response)

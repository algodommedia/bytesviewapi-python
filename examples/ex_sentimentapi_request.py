from bytesviewapi import BytesviewapiClient


api = BytesviewapiClient(api_key='API Key')

response = api.sentiment_api(data = {0: "we are good here"}, lang = "en")
print(response)

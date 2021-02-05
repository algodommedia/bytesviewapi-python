from bytesviewapi import BytesviewApiClient
import os


api_key = os.environ.get("TOKEN")

api = BytesviewApiClient(api_key=str(api_key))

response = api.sentiment_api(data = {0: "this is good"}, lang = "en")
print(response)


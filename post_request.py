from bytesviewapi import BytesviewapiClient


api = BytesviewapiClient(api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im5hbXJhdGFAYWxnb2RvbW1lZGlhLmNvbSJ9.ceDtxy7gbSSI1t3lrokTBMNajge7oPrmo07R7phKRI8')

a = api.sentiment_api(data = {0: "we are good here"}, lang = "en")
print(a)

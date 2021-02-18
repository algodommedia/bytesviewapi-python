import json
import time

def post(request_method, URL, header, payload, proxies, request_timeout):
    if proxies is None:
        return request_method.post(URL, auth=header, timeout=request_timeout, data=json.dumps(payload, indent = 4))
    else:
        return request_method.post(URL, auth=header, timeout=request_timeout, data=json.dumps(payload, indent = 4), proxies = proxies)

def get(request_method, URL, header, payload, proxies, request_timeout):
    if proxies is None:
        return request_method.get(URL, auth=header, timeout=request_timeout)
    else:
        return request_method.get(URL, auth=header, timeout=request_timeout, proxies = proxies)


def MaxRetries(response, max_retries, retry_delay, request_method, URL, header, payload, proxies, request_timeout):
    while (max_retries):
        time.sleep(retry_delay)
        response = post(request_method, URL, header, payload, proxies, request_timeout)
        if response.status_code!=500:
            break
        max_retries-=1
    return response



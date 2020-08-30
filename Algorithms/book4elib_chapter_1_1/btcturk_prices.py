import time, base64, hmac, hashlib, requests, json

base = "https://api.btcturk.com"
method = "/api/v2/ticker"
uri = base+method

result = requests.get(url=uri)
result = result.json()
print(json.dumps(result, indent=2))

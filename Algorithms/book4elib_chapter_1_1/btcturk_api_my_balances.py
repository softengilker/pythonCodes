import time, base64, hmac, hashlib, requests, json

base = "https://api.btcturk.com"
method = "/api/v1/users/balances"
uri = base+method

apiKey = "12d553ed-a0a6-4f9b-828f-57b9be1d2f5e"
apiSecret = "uzT63vyYP5DkQx1qznHY+1ARV2DZ//Fq"
apiSecret = base64.b64decode(apiSecret)

stamp = str(int(time.time())*1000)
data = "{}{}".format(apiKey, stamp).encode("utf-8")
signature = hmac.new(apiSecret, data, hashlib.sha256).digest()
signature = base64.b64encode(signature)
headers = {"X-PCK": apiKey, "X-Stamp": stamp, "X-Signature": signature, "Content-Type" : "application/json"}

result = requests.get(url=uri, headers=headers)
result = result.json()
print(json.dumps(result, indent=2))

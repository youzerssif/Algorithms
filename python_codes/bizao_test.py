# import requests



# payload = {
#   "Authorization": "Bearer 12345dxj-zd56-323c-85e9-d5v8h3s5b0",
#   "Accept": "application/json",
#   "country-code": "ci",
#   "mno-name": "orange",
#   "lang": "fr",
#   "channel": "web"
# }

# r = requests.post('https://api.bizao.com/mobilemoney/v1', params=payload)
# print(r.status_code)
# print(r.content)

import requests
payload = {
  "Authorization": "Basic TjJ4ZTd4emsyNUZaRW5TMFlnbWxEMTBhOnhwUERza0JJOUdLcGJQamtISnJBTjZRYQ==",
  "content-type": "application/x-www-form-urlencoded"
}

# data = ' { "currency": "XOF", "order_id": "Merchant_Order_id_4", "amount": 10, "state": "param1%3Dvalue1%26param2%3Dvalue2", "return_url": "Your-return_url", "cancel_url": "Your-cancel_url", "reference": "Your-reference" } '

response = requests.post('https://api.bizao.com/token', params=payload)

print(response.status_code)
print(response.content)
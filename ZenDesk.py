import requests
from requests.auth import HTTPBasicAuth
import json

subdomain = "freelance-0000"
email = "example@gmail.com/token"
api_token = "token"
ticket_id = 1

url = "https://" + subdomain + ".zendesk.com/api/v2/tickets/" + str(ticket_id) + ".json"

headers = {
    "Content-Type": "application/json"
}

data = {
    "ticket": {
        "tags": ["new_feature_stackholder", "Malware"],
        "priority":"high",
        "type" : "task" ,
        "requester": { "name": "arasriver", "email": "example@gmail.com" },
        "comment":  { "body": "Please press play on tape now"}
    }
}

response = requests.put(
    url,
    auth=HTTPBasicAuth(email, api_token),
    headers=headers,
    data=json.dumps(data)
)



print("Status Code:", response.status_code)
try:
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print("Error parsing response:", e)



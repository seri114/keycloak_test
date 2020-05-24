import requests
import json

url = "http://localhost:8080/auth/realms/master/protocol/openid-connect/token"

payload = "grant_type=password&client_id=admin-cli&client_secret=passwword&username=admin&password=Pa55w0rd"
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

token=response.json()["access_token"]

url = "http://localhost:8080/auth/admin/realms/master/users"
headers = {'authorization': f"Bearer {token}"}
response = requests.request("GET", url, headers=headers)

#print(json.dumps(response.json(), indent=2))

for u in response.json():
    if u["username"] == "test":
        print(u)
        u["attributes"]["test2"] = "test2"
        headers = {
            'authorization': f"Bearer {token}",
            'content-type' : 'application/json'}
        url = f"http://localhost:8080/auth/admin/realms/master/users/{u['id']}"
        response = requests.request("PUT", url, headers=headers, json=u)
        print(response.text)
        
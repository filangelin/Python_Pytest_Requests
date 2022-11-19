import requests


create={
  "id": 11,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "my doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response=requests.post("https://petstore.swagger.io/v2/pet", json=create, headers={"Content-Type": "application/json"})
print(f"1.Add a new pet\n"+response.text) 

change={
  "id": 11,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "No, my doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response=requests.put("https://petstore.swagger.io/v2/pet", json=change, headers={"Content-Type": "application/json"})
print(f"2.Update an existing pet\n"+response.text) 

response=requests.get("https://petstore.swagger.io/v2/pet/11")
print(f"3.Find pet by ID\n"+response.text) 
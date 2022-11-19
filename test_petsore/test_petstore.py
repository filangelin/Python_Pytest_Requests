import pytest
import requests

def test_status_code():
    url = "https://petstore.swagger.io/v2/pet/11"
    response=requests.get(url)
    assert response.status_code==200

def test_check_response():
    url = "https://petstore.swagger.io/v2/pet/11"
    response=requests.get(url).json()
    assert response["name"]=="No, my doggie"

@pytest.mark.parametrize("key, value, id", [("name", "No, my doggie", 11), ("status", "available", 11)])
def test_piece_of_body(key, value, id):
    url = f"https://petstore.swagger.io/v2/pet/{11}"
    response=requests.get(url).json()
    assert response[key]==value

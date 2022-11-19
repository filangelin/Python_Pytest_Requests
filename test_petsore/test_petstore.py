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
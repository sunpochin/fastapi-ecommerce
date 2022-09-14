from ssl import SSL_ERROR_SSL, SSLSocket
# from starlette.testclient import TestClient
from fastapi.testclient import TestClient
import requests

from sql_app.main import app
from sql_app.main import crud, get_db
import json

client = TestClient(app)


def test_songs(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"name": "sql_app"}


def test_get_users(test_app):
    response = test_app.get("/users")
    print('hahaha')
    resjson = response.json()
    assert response.json()[0]['email'] == "sunpochin@gmail.com"
    assert response.json()[0]['id'] == 1
    # assert len(resjson[0]['items']) == 7
#   assert response.json()[0]['items'] == 1
    assert response.status_code == 200


def test_add(test_app):
    response = requests.get('http://localhost:8000/deleteitems')

    response = requests.post('http://localhost:8000/users/1/items', json={
        "id": 78912,
        "title": "Jason Sweet",
        "Quantity": 1,
        "Price": 18.00
    })
    response = requests.get('http://localhost:8000/items')
    assert response.json() == "haha"
    # assert response.json()['id'] == "haha"

    test_add_item = {"id": 100, "title": "title3"}

    # response = test_app.post("/users/1/items",
    #     {"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"} )
    # assert response.json() == "haha"
    # assert response.json() == "haha"

    # assert response.status_code == 200
    # db = get_db()
    # users = crud.get_users(db)
    # print('users: ', users)

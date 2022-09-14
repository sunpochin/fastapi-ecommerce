from ssl import SSL_ERROR_SSL, SSLSocket
from starlette.testclient import TestClient
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
    assert len(resjson[0]['items']) == 7
#   assert response.json()[0]['items'] == 1
    assert response.status_code == 200


# def test_items(test_app):
#   response = test_app.get("/users/1/items")
#   assert response.json() == "haha"
#   assert response.status_code == 200
#   db = get_db()
#   users = crud.get_users(db)
#   print('users: ', users)

def test_add(test_app):
    test_add_item = {"id": "something",
                     "title": "something else",
                     "description": "item.description",
                     "price": 1,
                     }
    response = test_app.post("/users/1/itemshahaha", test_add_item)
#   assert response.json() == "haha"
    assert response.json() == "haha"

    assert response.status_code == 200
    db = get_db()
    users = crud.get_users(db)
    print('users: ', users)

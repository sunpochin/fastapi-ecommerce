from starlette.testclient import TestClient

from sql_app.main import app

client = TestClient(app)

def test_songs(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"name": "sql_app"}

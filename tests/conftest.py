import pytest
from starlette.testclient import TestClient
import requests

from sql_app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    return client  # testing happens here


def pytest_sessionstart(session):
    response = requests.get('http://localhost:8000/deleteallitems')
    print('BEFORE')

import pytest
from starlette.testclient import TestClient

from sql_app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    return client  # testing happens here

import pytest
from urlshortener.app import app

@pytest.fixture
def client():
    client = app.test_client()
    yield client 
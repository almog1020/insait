import pytest
from server import app

@pytest.fixture()
def client():
    return app.test_client()

def test_ask(client):
    response = client.post('/ask', json={
        "question": "What is python?"
    })
    assert response.status_code == 200


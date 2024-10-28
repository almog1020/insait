import pytest
from insait.server import app, setup_app


@pytest.fixture()
def mock_environment_variables(monkeypatch):
    # Usually these would be kept as a secret, but because cicd is out of the scope of this exercise, we will put
    # it directly here.
    monkeypatch.setenv("API_KEY", "sk-svcacct-zUCqdCSPk-uoeQFWj9VJwPuE78PNR5j_16OIiULwqy46w2nW5H_u8hZwa3EhttNFkXFNyT3BlbkFJSg1tHsI9fs7vCHWFF3ctTeb_VYGXP1Ok1EloFqTVIlLuw5l6H5wH7KSu2-6T8yvfqUFAA")
    monkeypatch.setenv("DB_CONNECTION_STRING", "postgresql://Almog:1999@127.0.0.1:5432/insait")


@pytest.fixture()
def client(mock_environment_variables):
    app.debug = True
    setup_app()
    return app.test_client()

def test_ask(client):
    response = client.post('/ask', json={
        "question": "What is python?"
    })
    assert response.status_code == 200
    assert response.get_json() != {"question": None}


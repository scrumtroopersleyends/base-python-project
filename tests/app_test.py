from app import create_app
import pytest

@pytest.fixture
def app():
    app = create_app()
    return app

def test_hello(app, client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'{"saludo":"Hello World"}\n'


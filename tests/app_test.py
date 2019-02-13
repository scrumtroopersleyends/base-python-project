from .source import src
import pytest


@pytest.fixture
def app():
    app = src.create_app()
    return app


def test_hello(app, client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'{"saludo":"Hello World"}\n'

        

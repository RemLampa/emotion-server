import pytest
from src.app import app


@pytest.fixture(scope='module')
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)

    return test_client


def test_index(client):
    response = client.get('/')

    assert response.data == b'Hello World!'


def test_emotion(client):
    response = client.get('/emotion/')

    assert response.data == b'Hello Emotion!'

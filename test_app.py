import os

def test_api_key():
    assert os.environ["API_KEY"] == "secret"
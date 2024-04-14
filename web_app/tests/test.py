import pytest

from web_app.app import *
from web_app.app import app

@pytest.fixture

def client():
    
    app.config.update({
        
        "TESTING" : True,
    })
    with app.test_client() as client:
        yield client


def test_sanity_check(client):

    expected = True
    actual = True
    assert actual == expected, "Expected True to be equal to True!"

def test_sanity_check2(client):

    expected = True
    actual = True
    assert actual == expected, "Expected True to be equal to True!"

def test_home_page(client):

    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Melody Note Finder" in response.data

def test_submit_page(client):

    response = client.get("/submit")
    assert response.status_code == 200
    assert b"Add Melody" in response.data


import pytest
import os

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

def test_view_page(client):

    response = client.get("/view")
    assert response.status_code == 200
    assert b"Your Melodies" in response.data

def test_analyze_page(client):

    response = client.get("/analyze/1234567")
    assert response.status_code == 200
    assert b"Analysis" in response.data

def test_running_in_docker(client):
    assert os.path.exists('/.dockerenv') == False


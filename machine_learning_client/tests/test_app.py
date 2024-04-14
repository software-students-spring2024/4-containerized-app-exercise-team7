from machine_learning_client.app import app
import pytest
import io


@pytest.fixture

def client():
    
    app.config.update({
        
        "TESTING" : True,
    })
    with app.test_client() as client:
        yield client
        
def test_no_file(client):
    
    response = client.post('/upload', data={})
    assert response.status_code == 400
    assert 'no file' in response.get_json()['error']
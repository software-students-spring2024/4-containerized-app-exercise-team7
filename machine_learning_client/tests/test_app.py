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
    

def test_empty_filename(client):
    
    data = {'file': (io.BytesIO(b"some initial binary data: \x00\x01"), '')}
    
    response = client.post('/upload', data=data)
    assert response.status_code == 400
    assert 'No File' in response.get_json()['error']
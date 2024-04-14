from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient
import librosa
from dotenv import find_dotenv, load_dotenv
import os
import io

load_dotenv()

app = Flask(__name__)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

# set up mongo 
# uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/?retryWrites=true&w=majority&appName=Cluster0&tlsAllowInvalidCertificates=true"
# mongo_client = MongoClient(uri)
mongo_client = MongoClient('mongodb://mongo_container:27017/')
db = mongo_client.get_database("proj4")
audio_collection = db.get_collection("audio_features")


def extract_audio_feature(audio_file):
    
    y, sr = librosa.load(audio_file)
    
   # trimmed, index = librosa.effects.trim(y, top_db=20)
    
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    
    # Tempo estimate
    
    temp = librosa.beat.tempo(y=y, sr=sr)[0]
    
    #beat tracking 

    
    #tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    #beat_times = librosa.frames_to_time(beats, sr =sr)
    
    feature ={
        'mfcc': mfcc.tolist(),
        'temp': temp,
    }
    
    return feature

@app.route('/upload', methods=['POST'])
def audio_file():
    if 'file' not in request.files:
        return jsonify({'error': 'no file'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No File'}), 400
    
    if not file.filename.endswith(('.mp3', '.wav')):
        return jsonify({'error': 'File not supported'}), 400
    
    if file:
        try:
            fn = file.filename
            audio_features = extract_audio_feature(io.BytesIO(file.read()))
        
            data={
                'filename': fn,
                'features': audio_features
                }
            audio_collection.insert_one(data)
        
            return jsonify({'message': 'Upload Successful!'}), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)

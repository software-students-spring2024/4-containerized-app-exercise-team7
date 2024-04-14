from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient
import librosa
import os
import io

app = Flask(__name__)

# set up mongo 
mongo_client = MongoClient('mongodb+srv://proj4:sweproj4@proj4.u34b77v.mongodb.net/')
db = mongo_client['proj4']  
AudioFeature = db['audio_features']  

def extract_audio_feature(audio_file):
    
    y, sr = librosa.load(audio_file)
    
   # trimmed, index = librosa.effects.trim(y, top_db=20)
    
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    
    # Tempo estimate
    
    temp = librosa.beat.tempo(y=y, sr=sr)[0]
    
    #beat tracking 

    
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beats, sr =sr)
    
    feature ={
        'mfcc': mfcc.tolist(),
        'temp': temp,
        'tempo': tempo,
        'beats': beats.tolist()    
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
                'feature': audio_features
                }
            AudioFeature.insert_one(data)
        
            return jsonify({'message': 'Upload Successful!'}), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)

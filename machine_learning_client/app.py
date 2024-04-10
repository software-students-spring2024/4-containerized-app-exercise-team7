from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient
import librosa
import os

app = Flask(__name__)

# set up mongo 
mongo_client = MongoClient('mongodb+srv://proj4:sweproj4@proj4.u34b77v.mongodb.net/')
db = mongo_client['proj4']  # db name
AudioFeature = db['audio_features']  # collection name


def extract_audio_feature(audio_file):
    
    y, sr = librosa.load(audio_file)
    
    feature = librosa.feature.mfcc(y=y, sr=sr)
    
    return feature.tolist()

@app.route('/upload', methods=['POST'])
def audio_file():
    if 'file' not in request.files:
        return jsonify({'error'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        
        return jsonify({'error': 'No File'}), 400
    
    if file:
        
        fn = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], fn)
        file.save(file_path)
        
        audio_features = extract_audio_feature(file_path)
        
        data={
            'filename': fn,
            'features': audio_features
            }
        AudioFeature.insert_one(data)
        
        return jsonify({'message': 'Upload Successful!'}), 200
    
#@app.route('/audio_features', method=['GET'])
#def get_audio_features():
    
if __name__ == '_main_':
    app.run(debug=True, port=5001)
        
        
    
    

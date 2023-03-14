import os
import time
import requests
import base64
import json

url = 'http://koeiromap-api.rinna.jp/api/inference/'
FILE_NAME = 'voice.wav'
DATA_DIR = 'data/koeiro'

def say(speacker_x, speaker_y, style, res):
    start_time = time.time()
    print(f"Recording started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    text = res
    payload = {
        'text': text,
        'speaker_x': speacker_x,
        'speaker_y': speaker_y,
        'style': style,
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    data = response.json()
    wav = base64.b64decode(data['audio'].split(',')[1])
    file_path = os.path.join(DATA_DIR, FILE_NAME)
    with open(file_path, 'wb') as f:
        f.write(wav)

    with open(file_path, 'rb') as f:
        # do something with the file
        pass
    
    end_time = time.time()
    print(f"Recording ended at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
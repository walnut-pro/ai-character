import time
import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

def transcribe_audio(file_path):
    start_time = time.time()
    print(f"Recording started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    # 音声ファイルを読み込む
    with open(file_path, "rb") as audio_file:
        # OpenAI APIを用いて音声をテキストに変換する
        transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file)
    
    # 出力先のディレクトリを作成する
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    json_dir_path = os.path.join(base_dir, "../data/whisper")
    if not os.path.exists(json_dir_path):
        os.makedirs(json_dir_path)
    
    # 変換結果をJSONファイルに保存する
    json_path = os.path.join(json_dir_path, "transcript.json")
    with open(json_path, "w") as json_file:
        json.dump(transcript["text"], json_file, indent=4, ensure_ascii=False)
        
    end_time = time.time()
    print(f"Recording ended at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")

    return transcript["text"]

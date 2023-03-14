import os
import subprocess
import time

FILE_NAME = 'voice.wav'
DATA_DIR = 'data/koeiro'

def play_voice():
    start_time = time.time()
    print(f"Recording started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    file_path = os.path.join(DATA_DIR, FILE_NAME)
    # 再生コマンドを生成する
    command = f"afplay {file_path}"
    # コマンドを実行する
    subprocess.run(command, shell=True)

    end_time = time.time()
    print(f"Recording ended at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")

if __name__ == "__main__":
    play_voice()

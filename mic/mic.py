import sounddevice as sd
import soundfile as sf
import os

def record_audio(duration=5):
    FORMAT = 'PCM_16'
    CHANNELS = 1
    RATE = 44100
    FILE_NAME = 'audio.wav'
    DATA_DIR = 'data/whisper'

    data = sd.rec(int(RATE * duration), samplerate=RATE, channels=CHANNELS)
    sd.wait()

    file_path = os.path.join(DATA_DIR, FILE_NAME)
    sf.write(file_path, data, RATE, subtype=FORMAT)
    return data

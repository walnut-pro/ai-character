import json
from transcription.whisper import transcribe_audio
from speak.playvoice import play_voice
from speak.koeiromap import say
from chat.chatgpt import chatbot
from mic.mic import record_audio

print("Choose a character:")
with open('data/character/attribute.json', 'r') as f:
    data = json.load(f)
    for i, char in enumerate(data.keys()):
        print(f"{i+1}. {char}")
    char_choice = input("Enter the number of the character you want to choose: ")
    char_name = list(data.keys())[int(char_choice)-1] if char_choice.isdigit() and int(char_choice) in range(1,len(data.keys())+1) else "kanata"
    speaker_x = data[char_name]['speaker_x']
    speaker_y = data[char_name]['speaker_y']
    style = data[char_name]['style']

print("loading...")
print('record')
record_audio()
print('transrate')
text = transcribe_audio("data/whisper/audio.wav")
print('chatgpt')
res = chatbot(text)
print('create model')
# # キャラクターを作成
say(speaker_x, speaker_y, style, res)
print('play')
# # playvoice.pyを実行して音声を再生
play_voice()

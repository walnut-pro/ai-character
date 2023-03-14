import time
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

def chatbot(text):
  start_time = time.time()
  print(f"Recording started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
  response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "あなたは配信活動をしている女の子です。一人称は私です。タメ口で、友達と話しているような口調にしましょう。"},
          {"role": "user", "content": text}])

  end_time = time.time()
  print(f"Recording ended at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
  return response["choices"][0]["message"]["content"]

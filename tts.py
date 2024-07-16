import os
import streamlit as st

from pathlib import Path
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = st.secrets.openai_api_key
client = OpenAI()

VOICES = ("alloy", "echo", "fable", "onyx", "nova", "shimmer")
FORMATS = ("wav", "flac", "mp3", "aac")

def transcribe(text: str, file_name: str, voice: str):
    speech_file_path = Path(__file__).parent / file_name
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text
    )

    response.write_to_file(speech_file_path)

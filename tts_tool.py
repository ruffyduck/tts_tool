import os
import atexit
import streamlit as st
from tts import transcribe, VOICES, FORMATS
from pathlib import Path

def clean_cache():
    speech_file_path = Path(__file__).parent

    for file in os.listdir(speech_file_path):
        _, extension = os.path.splitext(file)
        extension = extension[1:]

        if(extension in FORMATS):
            os.remove(speech_file_path / file)

def get_mime(extension: str) -> str:
    match(extension):
        case "wav" | "aac":
            return f'audio/{extension}'
        case "flac":
            return 'audio/x-flac'
        case "mp3":
            return 'audio/mpeg'


st.title('OpenAI TTS Tool')

atexit.register(clean_cache)
clean_cache()

with st.form("tts_form"):
    text = st.text_area(label="Text to be spoken", value="Text")
    st.info("Text can be anotated with *Markdown* for **emphasis**. Formatted text will be displayed on generate")

    st.empty()
    extension = st.selectbox('Select Format', FORMATS)
    voice = st.selectbox("Select Voice", VOICES)

    submitted = st.form_submit_button(label="Generate")

if(submitted):
    name = f"speech.{extension}"
    transcribe(text, name, voice)

    with open(name, 'rb') as audio:
        print(get_mime(extension))
        st.audio(audio, format=get_mime(extension), autoplay=False)
        st.empty()
        st.markdown(f"{text}")
        st.empty()
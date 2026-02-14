from gtts import gTTS
import os

def generate_voice(script):
    os.makedirs("audio", exist_ok=True)
    audio_path = "audio/voice.mp3"

    tts = gTTS(text=script, lang="en")
    tts.save(audio_path)

    return audio_path

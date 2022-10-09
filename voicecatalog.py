import speech_recognition as sr
import pyaudio
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)

for voice in voices:
    print(voice)
 #print ("hola");
import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit 
name= 'cutrana'

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print('escuchando........')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace('name', '')
                print(rec)

    except:
        pass

    return rec

def run():
    rec= listen()
    if 'reporduce' in rec:
        music = rec.replace('reporduce','')
        talk('reploduciendol' +music)
        pywhatkit.playonyt(music)

run()        

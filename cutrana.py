 #print ("hola");
import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit 
import urllib.request, urllib3
import json

name= 'cutrana'
key = 'AIzaSyDx_GXlaa2deOREuRZJon_8Y6Y06uwepis'

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
                rec = rec.replace(name, '')
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

    if 'cuantos subs tiene' in rec:
        name_subs = rec.replace('cuantos subs tiene','').strip()
        datoz = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=' + name_subs.strip() + '&key=' + key).read()
        subs = json.loads(datoz)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs + "tiene {:,d}".filter(int(subs))+ "subscriptores")
run()        

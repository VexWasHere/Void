import pyttsx3
import keyboard
import sys
import speech_recognition as sr
import pyaudio
import winsound
import socket
import time

engine = pyttsx3.init()

newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


winsound.PlaySound('beep.wav', winsound.SND_FILENAME)

#When microphone is functional, speech to text will be added here. 
init_rec = sr.Recognizer()
print("Let's speak!!")
with sr.Microphone() as source:
    audio_data = init_rec.record(source, duration=5)
    print("Recognizing your text.............")
    micData = init_rec.recognize_google(audio_data)
    print("You:", micData)
    
    def response():
         if "hello" in micData:
              engine.say("Hello sonny boy")

    response()


engine.runAndWait()

while True:
        if keyboard.is_pressed('alt + n'):
            print("Goodbye!")
            sys.exit()

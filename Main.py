import speech_recognition as sr
from time import ctime
import time
import os
import win32com.client as wincl
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

def jarvis(data):
    if "how are you" in data:
        speak.Speak("Good, How are you")
    
    if "good" in data:
        speak.Speak("Good Sir")
    elif "bad" in data:
        speak.Speak("I hope you feel better sir") # Continue converstaion later

    if "what time is it" in data:
        speak.Speak(ctime())
        print(ctime)
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak.Speak("Hold on Sir, I will show you where " + location + " is.")
        wb.open("https://www.google.com/maps/place/" + location + "/&amp;")

    if "definiton of" in data:
        data = data.split(" ")
        word = data[2]
        url = "https://www.google.com.tr/search?q={}".format(word) 
        speak.Speak("Hold on Sir, I will show you what " + word + " means.")
        wb.open(url)

    if "stop" in data:
        exit()
    
    if "quit" in data:
        exit()

    if "exit" in data:
        exit()

    if "bye" in data:
        exit()
 
# initialization
time.sleep(2)
speak.Speak("Hi Sir, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
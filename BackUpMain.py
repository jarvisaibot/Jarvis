import speech_recognition as sr
from time import ctime
import time
import os
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
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
        speak.Speak("I am fine")
 
    if "what time is it" in data:
        speak.Speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak.Speak("Hold on Sir, I will show you where " + location + " is.")
        os.system("https://www.google.com/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
speak.Speak("Hi Sir, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
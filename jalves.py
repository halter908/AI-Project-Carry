
import pyttsx3
from pyttsx3 import engine
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")

MASTER = "Carry"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour =  int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morining" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)

    # speak("I am carry. How can i  help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail(bksanju25@gmail.com, to, content)
    server.close()
# speak("Initializing Jarvis....")
wishMe()
query =  takeCommand()



if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("Wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")
        url = "youtube.com"
        webbrowser.get('edge').open('http://www.microsoft.com')
elif 'open google' in query.lower():
        webbrowser.open("google.com")
        url = "google.com"
        webbrowser.get('edge').open('http://www.microsoft.com')

elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\sanju viswakarma\\Downloads\\music"
    songs = os.listdir(songs_dir) 
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0])) 

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")
elif 'open code' in query.lower():
    codePath = "C:\\Users\\sanju viswakarma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
elif 'email to carry' in query.lower():
    try:
        speak("What should I send")
        content = takeCommand()
        to = "bksanju25@gmail.com"
        sendEmail(to, content)
        speak("Email has been send successfully")

    except Exception as e:
        print(e)
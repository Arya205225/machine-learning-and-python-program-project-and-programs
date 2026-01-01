import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time


def sptext():
    recognition=sr.Recognition()
    with sr.microphone() as source:
        print("listening..........")
        recognition.adjust_for_ambient_noise(source)
        audio=recognition.listen(source)
        
        try:
            print("recognition.......") 
            data=recognition.recognizer_google(audio)
            return data
        except sr.unknownvalueError:
            print("Not understand")


def speechtx(x):
    engine=pyttsx3.init()
    voice=engine.getproperty('voice')
    engine.setproperty('voice',voice[0].id)
    rate=engine.getproperty('rate')
    engine.setproperty('rate',150)
    engine.say(x)
    engine.runAndwait()
    
if __name__ == '__main__':
    if sptext().lower()=="hello":
        speechtx("hello sir i am bob how can i help you")
        while True:
            data1=sptext().lower()
            if"your name" in data1:
                name="my name is bob"
                speechtx(name)
            elif "old are you " in data1:
                age="I am a machine so my age is not define"
                speechtx(age)
            elif 'time' in data1:
                time=datetime.datetime.now().strftime("%I%m%P")
                speechtx(time)
            elif'google' in data1:
                webbrowser.open("http://www.google.com/")
                speechtx("google is open now")
                
            elif 'youtube' in data1:
                webbrowser.open("http://www.youtube.com/")
                speechtx("youtube is open now")
            
            elif 'facebook' in data1:
                webbrowser.open("http://www.facebook.com/")
                speechtx("facebook is open now")
            
            elif 'instagram' in data1:
                webbrowser.open("http://www.instagram.com/")
                speechtx("instagram is open now")
            
            elif 'twitter' in data1:
                webbrowser.open("http://www.twitter.com/")
                speechtx("twitter is open now")
            
            elif 'linkedin' in data1:
                webbrowser.open("http://www.linkedin.com/")
                speechtx("linkedin is open now")
            
            elif 'gmail' in data1:
                webbrowser.open("http://www.gmail.com/")
                speechtx("gmail is open now")
            
            elif 'amazon' in data1:
                webbrowser.open("http://www.amazon.com/")
                speechtx("amazon is open now")
            
            elif 'whatsapp' in data1:
                webbrowser.open("https://web.whatsapp.com/")
                speechtx("whatsapp is open now")
            elif 'joke' in data1:
                joke_1=pyjokes.get_joke (language="en",category="all")
                speechtx(joke_1)
            
            elif 'exit' in data1:
                speechtx("thanks for using me")
                break
                
            
else:
    print("thanks")        
            
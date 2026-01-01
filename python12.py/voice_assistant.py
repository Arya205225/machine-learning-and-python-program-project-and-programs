import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time

def sptext():
    recognizer = sr.Recognizer()

    

    mic_index = 3   

    with sr.Microphone(device_index=mic_index) as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}")
            return data
        except sr.UnknownValueError:
            print("Sorry, I didn’t understand.")
            return ""
        except sr.RequestError:
            print("Speech service unavailable.")
            return ""

    

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    print("Say 'hello' to start.")
    

    if "hello" in sptext().lower() :
        speechtx("Hello sir, I am Bob. How can I help you?")
        while True:
            data1 = sptext().lower()
            if data1 == "":
                continue

            if "your name" in data1:
                speechtx("My name is Bob.")
            elif "old are you" in data1:
                speechtx("I am a machine, so my age is not defined.")
            elif "time" in data1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(f"The time is {current_time}")
            elif "google" in data1:
                webbrowser.open("http://www.google.com/")
                speechtx("Google is open now.")
            elif "youtube" in data1:
                webbrowser.open("http://www.youtube.com/")
                speechtx("YouTube is open now.")
            elif "facebook" in data1:
                webbrowser.open("http://www.facebook.com/")
                speechtx("Facebook is open now.")
            elif "instagram" in data1:
                webbrowser.open("http://www.instagram.com/")
                speechtx("Instagram is open now.")
            elif "twitter" in data1:
                webbrowser.open("http://www.twitter.com/")
                speechtx("Twitter is open now.")
            elif "linkedin" in data1:
                webbrowser.open("http://www.linkedin.com/")
                speechtx("LinkedIn is open now.")
            elif "gmail" in data1:
                webbrowser.open("http://www.gmail.com/")
                speechtx("Gmail is open now.")
            elif "amazon" in data1:
                webbrowser.open("http://www.amazon.com/")
                speechtx("Amazon is open now.")
            elif "whatsapp" in data1:
                webbrowser.open("https://web.whatsapp.com/")
                speechtx("WhatsApp is open now.")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="all")
                speechtx(joke_1)
            elif "exit" in data1 or "stop" in data1 or "bye" in data1:
                speechtx("Thanks for using me. Goodbye!")
                break
    else:
        print("You didn’t say 'hello'. Exiting.")
        
        

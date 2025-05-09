import pyttsx3 as pt
import webbrowser as wb
import speech_recognition as sr
import datetime as dt


#this function will take input (speech) from user and store it as string
def speech_listener():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) #removes extra noises from source
        audio = recognizer.listen(source)
        try:
            print('Recognised')
            data = recognizer.recognize_amazon(audio)
            print(data)
        except sr.UnknownValueError:
            print('unable to recognise')
speech_listener()


'''
# assistant/speaker.py

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Adjust speaking rate if needed
engine.setProperty('volume', 1.0)  # Volume: 0.0 to 1.0

def talk(text):
    print("Assistant:", text)  # For terminal display
    engine.say(text)
    engine.runAndWait()
    '''

# assistant/speaker.py
import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)  # Adjust speaking rate
    engine.setProperty('volume', 1.0)  # Volume: 0.0 to 1.0
    return engine

engine = init_engine()

def talk(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


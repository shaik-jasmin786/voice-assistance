

import speech_recognition as sr

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"You said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        command = ""
    except sr.RequestError:
        print("Speech service unavailable.")
        command = ""
    return command


